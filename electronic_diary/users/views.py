from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.template.context_processors import request
from django.views import View

from electronic_diary.users.forms import AuthUserForm
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'users/home.html', context)


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    redirect_authenticated_user = True

