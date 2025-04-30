# Line 47 & 53 Creats a custoum flag to be sent from views by Mohi(W1972510) 

from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProfileForm, ConfirmDeleteForm

def profile_view(request):
    user = request.user

    # Only show form if the user is authenticated, otherwise create empty
    if user.is_authenticated:
        profile_form = ProfileForm(instance=user)
    else:
        profile_form = None  # No form if user isn't logged in

    delete_form = ConfirmDeleteForm()

    if request.method == "POST":
        if user.is_authenticated and 'update_profile' in request.POST:
            profile_form = ProfileForm(request.POST, instance=user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect('profile')

        elif user.is_authenticated and 'delete_account' in request.POST:
            delete_form = ConfirmDeleteForm(request.POST)
            if delete_form.is_valid():
                password = delete_form.cleaned_data['password']
                if authenticate(username=user.username, password=password):
                    user.delete()
                    logout(request)
                    messages.success(request, "Your account has been deleted successfully.")
                    return redirect('home')
                else:
                    messages.error(request, "Incorrect password.")

    return render(request, 'user/profile.html', {
        'profile_form': profile_form,
        'delete_form': delete_form,
    })

# Dashboard views
def d_lead_dashboard_view(request):
    return render(request, "user/dLeadDashboard.html", {'is_dlead': True})

def engineer_dashboard_view(request):
    return render(request, "user/engineerDashboard.html")

def senior_dashboard_view(request):
    return render(request, "user/seniorDashboard.html", {'is_senior': True})

def team_lead_dashboard_view(request):
    return render(request, "user/teamLead_dashboard.html")
