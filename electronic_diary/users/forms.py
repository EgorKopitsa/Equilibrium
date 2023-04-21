from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomerUser


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomerUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'middle_name', 'username', 'email', 'gender', 'birth_date')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'Логин'})
            self.fields['email'].widget.attrs.update({"placeholder": "Электронная почта"})
            self.fields['first_name'].widget.attrs.update({'placeholder': 'Имя'})
            self.fields['last_name'].widget.attrs.update({'placeholder': 'Фамилия'})
            self.fields['middle_name'].widget.attrs.update({'placeholder': 'Отчество'})
            self.fields['gender'].widget.attrs.update({'placeholder': 'Пол'})
            self.fields['birth_date'].widget.attrs.update({'placeholder': 'Дата рождения'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class AuthUserForm(AuthenticationForm):

    class Meta:
        model = CustomerUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
