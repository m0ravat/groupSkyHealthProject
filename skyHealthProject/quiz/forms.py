#This file was coded by Barket Omar Sheikh (w2045831)

from django import forms
from captcha.fields import CaptchaField
from .models import Vote, Card

class QuizForm(forms.Form):
    def init(self, args, **kwargs):
        cards = kwargs.pop('cards', [])
        super(QuizForm, self).init(args, **kwargs)
        for card in cards:
            self.fields[f'card_{card.id}'] = forms.IntegerField(
                label=card.question_text,
                min_value=1, max_value=5,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate 1-5'})
            )
    captcha = CaptchaField()