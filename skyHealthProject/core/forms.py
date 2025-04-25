# Iqra Shah (w1973224)
from django import forms
from .models import User
from captcha.fields import CaptchaField

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
