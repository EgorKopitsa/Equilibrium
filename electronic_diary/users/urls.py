from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('profile/detail/<int:pk>/', UserDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserUpdateView.as_view(), name='profile_edit'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
