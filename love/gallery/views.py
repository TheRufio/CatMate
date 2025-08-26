from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('registration:login')
    
class GalleryView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("Test is completed")

class HomeView(LoginRequiredMixin, View):
    template = 'gallery/home.html'

    def get(self, request):
        return render(request, self.template)
    
class ProfileView(LoginRequiredMixin, View):
    template = 'gallery/profile.html'

    def get(self, request):
        return render(request, self.template)