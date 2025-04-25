
from django import forms
from .models import User, Department, Team
from captcha.fields import CaptchaField

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Your Department")
    team = forms.ModelChoiceField(queryset=Team.objects.none(), empty_label="Select Your Team")  # Start with no teams

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

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
