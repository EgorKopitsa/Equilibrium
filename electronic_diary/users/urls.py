from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
]
