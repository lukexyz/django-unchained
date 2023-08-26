
from allauth.account.forms import SignupForm
from django import forms

class AllauthSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1]
        if domain != "gmail.com":
            raise forms.ValidationError("Please use a Gmail account")
        return email
