from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import View, CreateView

from .forms import AuthUserForm, RegisterUserForm
from .models import CustomerUser


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'users/home.html', context)


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = AuthUserForm


class RegisterUserView(CreateView):

    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm

    # auto login after register
    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('/')

