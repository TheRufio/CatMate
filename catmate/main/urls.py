from django.urls import path
from .views import FindSomeoneView, CreateUserProfileView

app_name = 'main'
urlpatterns = [
    path('create-user-profile/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('find-someone/', FindSomeoneView.as_view(), name='find-someone')
]