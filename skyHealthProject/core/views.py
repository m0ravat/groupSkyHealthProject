# This file was coded by Iqra Shah w1973224
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm
from .models import Department, Team
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

def home_view(request):
    return render(request, 'homePage.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False  # Deactivate the user until email is verified
            user.save()

            # Generate token for email verification
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode()).decode()
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message = render_to_string('email/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            send_mail(mail_subject, message, 'no-reply@yourdomain.com', [user.email])

            # Redirect to email verification page
            return redirect('email_verification')  # You can show a message to the user here
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def email_verification(request):
    return render(request, 'email/email_verification.html')  # Page to inform user to check email

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)  # Log the user in after activation
        return redirect('login')  # Redirect to login page after successful activation
    else:
        return redirect('invalid_activation')  # Redirect to an error page if token is invalid

# def signup_view(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()  
#             login(request, user) 
            
    #         # Redirect based on user role
    #         if user.role == 'seniorManager':
    #             return redirect('senior_dashboard')
    #         elif user.role == 'teamLeader':
    #             return redirect('team_lead_dashboard')
    #         elif user.role == 'deptLeader':
    #             return redirect('d_lead_dashboard')
    #         else:
    #             return redirect('engineer_dashboard')
    # else:
    #     form = SignupForm()
    # return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            # Use email to find the user
            try:
                user = User.objects.get(email=email)  # Find user by email
                if user.check_password(password):  # Check password
                    login(request, user)
                    # Redirect to appropriate dashboard based on user role
                    if user.role == 'seniorManager':
                        return redirect('senior_dashboard')
                    elif user.role == 'teamLeader':
                        return redirect('team_lead_dashboard')
                    elif user.role == 'deptLeader':
                        return redirect('d_lead_dashboard')
                    else:
                        return redirect('engineer_dashboard')
                else:
                    form.add_error(None, "Invalid email or password")
            except User.DoesNotExist:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})