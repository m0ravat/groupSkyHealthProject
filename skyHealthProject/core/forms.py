#This file was coded by Iqra Shah (w1973224)
from django import forms
from django.contrib.auth.models import User 
from .models import User, Department, Team
from captcha.fields import CaptchaField

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Your Department")
    team = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="Select Your Team")

    role = forms.ChoiceField(
        choices=[("", "Select Your Role")] + User.Role_Choices,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'role', 'department', 'team', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already taken.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save() 
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()