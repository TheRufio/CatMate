from django.urls import path
from .views import RegistrationView, RegistrationConfirmView, LoginView, LogoutView
app_name = 'registration'

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('confirm/', RegistrationConfirmView.as_view(), name='confirm_registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]