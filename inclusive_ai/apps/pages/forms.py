from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError

class CustomSignupForm(SignupForm):
    consent = forms.BooleanField(label='Я даю согласие на обработку персональных данных', required=True)

    def clean_consent(self):
        if not self.cleaned_data.get('consent'):
            raise ValidationError('Вы должны дать согласие на обработку персональных данных.')
        return self.cleaned_data['consent']
