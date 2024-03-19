from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'name', 'second_name', 'email', 'password')


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('nickname', 'password')
#
