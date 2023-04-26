from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm, PasswordResetForm

from .models import CustomerUser


class CheckEmailForm(forms.Form):
    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and CustomerUser.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        return email


class UserRegisterForm(UserCreationForm, CheckEmailForm):
    """
    Форма регистрации пользователя
    """
    class Meta:
        model = CustomerUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'middle_name', 'username', 'email', 'gender', 'birth_date', 'avatar')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Придумайте свой логин'})
            self.fields['username'].label = 'Логин'
            self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Ваше имя'})
            self.fields["last_name"].widget.attrs.update({"placeholder": 'Ваша фамилия'})
            self.fields["middle_name"].widget.attrs.update({"placeholder": 'Ваше отчество'})
            self.fields["gender"].widget.attrs.update({"placeholder": 'Ваш пол'})
            self.fields["birth_date"].widget.input_type = 'date'
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class AuthUserForm(AuthenticationForm):
    """
    Форма авторизации пользователя
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы авторизации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserUpdateForm(forms.ModelForm, CheckEmailForm):
    """
    Форма обновления данных пользователя
    """
    class Meta:
        model = CustomerUser
        fields = ('first_name', 'last_name', 'middle_name', 'username', 'email', 'gender', 'birth_date')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserPasswordChangeForm(SetPasswordForm):
    pass


class UserForgotPasswordForm(PasswordResetForm):
    pass


class UserSetNewPasswordForm(SetPasswordForm):
    pass
