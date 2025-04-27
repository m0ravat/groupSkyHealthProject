# This file was coded by Iqra Shah w1973224
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from .models import Department, Team
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'homePage.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user after form is validated
            login(request, user)  # Automatically log the user in after signup
            
            # Redirect based on user role
            if user.role == 'seniorManager':
                return redirect('senior_dashboard')
            elif user.role == 'teamLead':
                return redirect('team_lead_dashboard')
            elif user.role == 'departmentLead':
                return redirect('d_lead_dashboard')
            else:
                return redirect('engineer_dashboard')
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)  # Corrected authentication method
            if user is not None:
                login(request, user)
                # Redirect to a dashboard depending on the user's role
                if user.role == 'seniorManager':
                    return redirect('senior_dashboard')
                elif user.role == 'teamLead':
                    return redirect('team_lead_dashboard')
                elif user.role == 'departmentLead':
                    return redirect('d_lead_dashboard')
                else:
                    return redirect('engineer_dashboard')  # Default to engineer dashboard if no specific role found
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})



