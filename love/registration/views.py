from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm, RegistationConfirmForm, LoginForm
from .models import CustomUser
from random import randint

class RegistrationView(View):
    form_class = RegistrationForm
    template = 'registration/registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            request.session['registration_data'] = form.cleaned_data
            confirmation_key = str(randint(100000,999999))
            request.session['confirmation_key'] = confirmation_key

            send_mail(
                subject="Confrim your registration",
                message=f"Here is your confirmation code: {confirmation_key}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )

            return redirect('registration:confirm_registration')

        return render(request, self.template, {'form': form})
    
class RegistrationConfirmView(View):
    form_class = RegistationConfirmForm
    template = 'registration/confirm.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['confirmation_key']
            real_code = request.session.get('confirmation_key')
            if entered_code == real_code:
                data = request.session.get('registration_data')
                if not data:
                    return redirect('registration:registration')
                user = CustomUser.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password1'],
                )
                request.session.pop('registration_data', None)
                request.session.pop('confirmation_key', None)
                return redirect('gallery:gallery')
        return render(request, self.template, {'form': form})
    
class LoginView(View):
    template = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('form valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gallery:home')
        return render(request, self.template, {'form': form})
    