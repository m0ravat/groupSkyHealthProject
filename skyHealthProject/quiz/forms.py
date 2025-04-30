from django import forms
from captcha.fields import CaptchaField
from .models import Card

class QuizForm(forms.Form):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        cards = kwargs.pop('cards', [])
        super(QuizForm, self).__init__(*args, **kwargs)
        for card in cards:
            self.fields[f'card_{card.id}'] = forms.IntegerField(
                label=card.question_text,
                min_value=1,
                max_value=5,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate 1-5'})
            )
