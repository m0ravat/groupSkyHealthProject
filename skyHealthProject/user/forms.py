from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# Forms made by Iqra for Hamza's profile page
class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']  # Fixed field names

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Email is already taken.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# Muhammad Hamza Khan w1996771
class ConfirmDeleteForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    captcha = CaptchaField()
