from django import forms
from django.core.validators import validate_email


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if validate_email(email):
            raise forms.ValidationError('Email invalid')

        return email
