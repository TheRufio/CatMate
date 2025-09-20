from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm, UserProfileNameForm
from .models import ChatMember, Chat, UserProfile, ChatProfile, Achievement, Inventory
from .choices import Specials
from gallery.models import Gallery
from marketplace.models import Item
from event.models import Events
from registration.models import CustomUser

class FindSomeoneView(LoginRequiredMixin, View):
    template_name = 'main/find-someone.html'
    def get(self, request):
        if not hasattr(request.user, "userprofile"):
            return redirect('main:create-user-profile')
        user_profile = UserProfile.objects.get(user=request.user)
        user_chats = Chat.objects.filter(chatmember__user=request.user)
        users_with_chats = CustomUser.objects.filter(
            chatmember__chat__in=user_chats
        ).exclude(pk=request.user.pk)
        recommend_users = UserProfile.objects.filter(
            interests__in=user_profile.interests.all()
        ).exclude(
            pk=user_profile.pk
        ).exclude(
            user__in=users_with_chats
        ).distinct()
        return render(request, self.template_name, {'recommend_users': recommend_users})
    
class CreateUserProfileView(LoginRequiredMixin, View):
    template_name = 'main/create-user-profile.html'

    def get(self, request):
        if hasattr(request.user, "userprofile"):
            return redirect('main:chats')

        userprofile = UserProfileForm()
        userprofilename = UserProfileNameForm()
        return render(request, self.template_name, 
                      {'userprofile_form': userprofile,
                       'userprofilename_form': userprofilename}
        )
    
    def post(self, request):
        userprofile = UserProfileForm(request.POST, request.FILES)
        userprofilename = UserProfileNameForm(request.POST)
        if userprofile.is_valid() and userprofilename.is_valid():
            profile = userprofile.save(commit=False)
            profile.user = request.user
            profile.save()
            userprofile.save_m2m()

            request.user.first_name = userprofilename.cleaned_data['first_name']
            request.user.last_name = userprofilename.cleaned_data['last_name']
            request.user.save()
            return redirect('main:chats') # must be chats
        
        return render(request, self.template_name, 
                      {'userprofile_form': userprofile,
                       'userprofilename_form': userprofilename}
        )

class ChatView(LoginRequiredMixin, View):
    template_name = 'main/chat.html'

    def get(self, request, id):
        chat = Chat.objects.get(id=id)
        return render(request, self.template_name, {'chat': chat})

@login_required
def create_chat(request, username):
    other_user = CustomUser.objects.get(username=username)
    chat = Chat.objects.create(
        name=f'{request.user.username} & {other_user.username}',
        special_type = Specials.NONE
    )
    ChatProfile.objects.create(
        chat=chat,
        coins=0,
        max_coins=0
    )
    ChatMember.objects.create(
        chat=chat,
        user=request.user,
        chat_avatar=request.user.userprofile.avatar,
        chat_username=request.user.username
    )
    ChatMember.objects.create(
        chat=chat,
        user=other_user,
        chat_avatar=UserProfile.objects.get(user=other_user).avatar,
        chat_username=other_user.username
    )
    return redirect('main:chats')

class ChatsView(LoginRequiredMixin, View):
    template_name = 'main/chats.html'

    def get(self, request):
        chats = Chat.objects.filter(chatmember__user=request.user)
        if not chats:
            messages.info(request, 'You don\'t have any chats yet')
        return render(request, self.template_name, {'chats': chats})


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'main/user-profile.html'

    def get(self, request, username):
        user_profile = CustomUser.objects.get(username=username)
        return render(request, self.template_name, {'user_profile': user_profile})