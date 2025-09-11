from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserProfileForm, UserProfileNameForm
from .models import ChatMember, Chat, UserProfile

class ChatsView(LoginRequiredMixin, View):
    template_name = 'main/chats.html'

    def get(self, request):
        chats = Chat.objects.filter(chatmember__user=request.user)
        if not chats:
            messages.info(request, 'You don\'t have any chats yet')
        return render(request, self.template_name, {'chats': chats})

class FindSomeoneView(LoginRequiredMixin, View):
    template_name = 'main/find-someone.html'
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        print(user_profile)
        recommend_users = UserProfile.objects.filter(
            interests__in=user_profile.interests.all()
        ).exclude(pk=user_profile.pk).distinct()
        return render(request, self.template_name, {'recommend_users': recommend_users})
    
class CreateUserProfileView(LoginRequiredMixin, View):
    template_name = 'main/create-user-profile.html'

    def get(self, request):
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

    def get(self, request, username):
        return render(request, self.template_name)