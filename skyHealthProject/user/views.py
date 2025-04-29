from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from captcha.fields import CaptchaField
from django import forms

# Confirm delete form (Password + CAPTCHA)
class ConfirmDeleteForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    captcha = CaptchaField()

#@login_required
def profile_view(request):
    user = request.user  # Logged-in user
    delete_form = ConfirmDeleteForm()  # Create empty delete form

    if request.method == "POST":
        if 'update_profile' in request.POST:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.profile.phone_number = request.POST.get('phone_number')
            user.profile.role = request.POST.get('role')
            user.save()
            user.profile.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')

        if 'delete_account' in request.POST:
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
        'user_profile': user,
        'delete_form': delete_form
    })
from django.contrib.auth.decorators import login_required

#@login_required
def d_lead_dashboard_view(request):
    return render(request, "user/dLeadDashboard.html")

#@login_required
def engineer_dashboard_view(request):
    return render(request, "user/engineerDashboard.html")

#@login_required
def senior_dashboard_view(request):
    return render(request, "user/seniorDashboard.html")

#@login_required
def team_lead_dashboard_view(request):
    return render(request, "user/teamLead_dashboard.html")
