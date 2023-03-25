from django.shortcuts import render
from django.template.context_processors import request
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'users/home.html', context)
