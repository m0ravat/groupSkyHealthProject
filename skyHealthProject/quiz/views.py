from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, Session, SessionAssignment, Vote
from .forms import QuizForm

def quiz_view(request):
    user = request.user if request.user.is_authenticated else None
    sessions = Session.objects.all()

    if request.method == 'POST':
        session_id = request.POST.get('session')
        new_session_name = request.POST.get('new_session_name')

        if new_session_name:
            session = Session.objects.create(name=new_session_name)
        else:
            session = get_object_or_404(Session, id=session_id)

        # Prevent assigning sessions to anonymous users
        if user:
            session_assignment, _ = SessionAssignment.objects.get_or_create(user=user, session=session)
        else:
            # You might need to handle anonymous users differently
            session_assignment = None

        form = QuizForm(request.POST, cards=Card.objects.all())
        if form.is_valid() and session_assignment:
            for card in Card.objects.all():
                rating = form.cleaned_data.get(f'card{card.id}')
                if rating is not None:
                    Vote.objects.create(
                        card=card,
                        session_assignment=session_assignment,
                        rating=rating,
                        progress=rating
                    )
            return redirect('quiz_success')
    else:
        form = QuizForm(cards=Card.objects.all())

    return render(request, 'quiz.html', {
        'form': form,
        'sessions': sessions
    })

def quiz_success(request):
    return render(request, 'quiz_success.html')
