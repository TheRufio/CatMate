from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Password do not match')
        return cleaned_data
    
class RegistationConfirmForm(forms.Form):
    confirmation_key = forms.CharField(
        widget=forms.widgets.NumberInput, 
        max_length=6)