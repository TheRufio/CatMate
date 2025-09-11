from django import forms
from .models import UserProfile
from registration.models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'age', 'gender', 'interests']
        widgets = {
            'interests': forms.CheckboxSelectMultiple,
        } 

class UserProfileNameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True