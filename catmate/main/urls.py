from django.urls import path
from .views import FindSomeoneView, CreateUserProfileView, ChatsView, ChatView

app_name = 'main'
urlpatterns = [
    path('create-user-profile/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('chats/', ChatsView.as_view(), name='chats'),
    path('chat/<str:username>', ChatView.as_view(), name='chat'),
    path('find-someone/', FindSomeoneView.as_view(), name='find-someone'),
]