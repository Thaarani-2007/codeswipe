# forms.py
from django import forms
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'github_url']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)  # Hash the password before saving
