from django.urls import path
from .views import FindSomeoneView, CreateUserProfileView, ChatsView, ChatView, UserProfileView
from .views import create_chat
app_name = 'main'
urlpatterns = [
    path('create-user-profile/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('chats/', ChatsView.as_view(), name='chats'),
    path('chats/chat-create/<str:username>', create_chat, name='chat-create'),
    path('chats/chat/<int:id>', ChatView.as_view(), name='chat'),
    path('find-someone/', FindSomeoneView.as_view(), name='find-someone'),
    path('user-profile/<str:username>', UserProfileView.as_view(), name='user-profile')
]