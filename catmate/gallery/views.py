from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class GalleryView(LoginRequiredMixin, View):
    template_name = 'gallery/gallery.html'
    
    def get(self, request):
        return render(request, self.template_name)

class AddMemoryView(LoginRequiredMixin, View):
    template_name = 'gallery/add_memory.html'

    def get(self, request):
        return render(request, self.template_name)
    
class AddGalleryView(LoginRequiredMixin, View):
    template_name = 'gallery/add_gallery.html'

    def get(self, request):
        return render(request, self.template_name)