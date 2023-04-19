from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomerUser


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(label="Электронная почта", max_length=254, widget=forms.EmailInput(attrs={"placeholder": "Электронная почта"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    gender = forms.CharField(label='Пол', max_length=1, widget=forms.TextInput(attrs={'placeholder': 'Пол'}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.TextInput(attrs={'placeholder': 'Дата рождения'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = CustomerUser
        fields = ('first_name', 'last_name', 'middle_name', 'username', 'email','gender', 'birth_date')


class AuthUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = CustomerUser
        fields = ('username', 'password')
