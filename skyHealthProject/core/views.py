# This file was coded by Iqra Shah w1973224
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm
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
            user.is_active = True
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message = render_to_string('email/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            send_mail(mail_subject, message, 'no-reply@yourdomain.com', [user.email])

            return redirect('email_verification')  
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def email_verification(request):
    return render(request, 'email/email_verification.html') 

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        if user.role == 'seniorManager':
            return redirect('senior_dashboard')
        elif user.role == 'teamLeader':
            return redirect('team_lead_dashboard')
        elif user.role == 'deptLeader':
            return redirect('d_lead_dashboard')
        else:
            return redirect('engineer_dashboard')
    else:
        return redirect('invalid_activation')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            try:
                user = User.objects.get(email=email)  
                if user.check_password(password): 
                    login(request, user)
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

# Done by Mohi (1972510)
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  
