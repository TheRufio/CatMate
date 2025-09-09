from django import forms
from .models import UserProfile
from registration.models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'age', 'gender', 'interests']
        widgets = {
            'intersts': forms.CheckboxSelectMultiple,
        } # might choice interests better way. Not ctr+mouse1

class UserProfileNameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']