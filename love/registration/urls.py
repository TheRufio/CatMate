from django.urls import path
from .views import RegistrationView, RegistrationConfirmView
app_name = 'registration'

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('confirm/', RegistrationConfirmView.as_view(), name='confirm_registration')
]