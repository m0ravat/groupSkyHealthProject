#This file was coded by Barket Omar Sheikh (w2045831)

from django.shortcuts import render, redirect
from .models import Card, Session, SessionAssignment, Vote
from .forms import QuizForm
from django.contrib.auth.decorators import login_required

@login_required
def quiz_view(request):
    user = request.user
    sessions = Session.objects.all()

    if request.method == 'POST':
        session_id = request.POST.get('session')
        new_session_name = request.POST.get('new_session_name')

        if new_session_name:
            session = Session.objects.create(name=new_session_name)
        else:
            session = Session.objects.get(id=session_id)

        session_assignment, created = SessionAssignment.objects.get_or_create(user=user, session=session)

        form = QuizForm(request.POST, cards=Card.objects.all())
        if form.is_valid():
            for card in Card.objects.all():
                rating = form.cleaned_data.get(f'card{card.id}')
                Vote.objects.create(
                    card=card,
                    session_assignment=session_assignment,
                    rating=rating,
                    progress=rating  
                )
            return redirect('complete')

    else:
        form = QuizForm(cards=Card.objects.all())

    return render(request, 'quiz.html', {
        'form': form,
        'sessions': sessions
    })

def quiz_success(request):
    return render(request, 'quiz_success.html')
