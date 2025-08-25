from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class GalleryView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("Test is completed")


class HomeView(LoginRequiredMixin, View):
    template = 'gallery/home.html'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, self.template)