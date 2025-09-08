from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm

class FindSomeoneView(LoginRequiredMixin, View):
    template_name = 'main/find-someone.html'
    def get(self, request):
        return render(request, self.template_name)
    
class CreateUserProfileView(LoginRequiredMixin, View):
    form_class = UserProfileForm
    template_name = 'main/create-user-profile.html'

    def get(self, request):
        user = request.user
        print(user)
        return render(request, self.template_name, 
                      {'user': user,
                       'form': self.form_class}
        )
