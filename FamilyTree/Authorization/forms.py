from Registration.models import User
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'password')