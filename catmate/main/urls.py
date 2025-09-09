from django.urls import path
from .views import FindSomeoneView, CreateUserProfileView, ChatsView

app_name = 'main'
urlpatterns = [
    path('create-user-profile/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('chats/', ChatsView.as_view(), name='chats'),
    path('find-someone/', FindSomeoneView.as_view(), name='find-someone'),
]