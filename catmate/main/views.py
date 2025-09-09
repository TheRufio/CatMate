from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm, UserProfileNameForm

class FindSomeoneView(LoginRequiredMixin, View):
    template_name = 'main/find-someone.html'
    def get(self, request):
        return render(request, self.template_name)
    
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
            request.user.lastname = userprofilename.cleaned_data['last_name']
            request.user.save()
            return redirect('main:find-someone') # must be chats
        
        return render(request, self.template_name, 
                      {'userprofile_form': userprofile,
                       'userprofilename_form': userprofilename}
        )