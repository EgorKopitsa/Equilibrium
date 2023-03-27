from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AuthUserForm(AuthenticationForm, forms.ModelForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')