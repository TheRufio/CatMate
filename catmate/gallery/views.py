from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class GalleryView(LoginRequiredMixin, View):
    template = 'gallery/gallery.html'
    
    def get(self, request):
        return render(request, self.template)
