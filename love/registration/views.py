from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import RegistrationForm

class RegistrationView(View):
    form_class = RegistrationForm
    template = 'registration/registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    