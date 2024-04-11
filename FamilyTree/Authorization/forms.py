from Registration.models import User
from django import forms

class LoginForm(forms.ModelForm):
    nickname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'login-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'login-input'}))
    class Meta:
        model = User
        fields = ('nickname', 'password')