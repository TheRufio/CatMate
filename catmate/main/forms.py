from django import forms
from .models import UserProfile
from registration.models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'age', 'gender', 'interests']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'profile-input profile-age'}),
            'interests': forms.CheckboxSelectMultiple(attrs={'class': 'profile_checkbox'}),
        } 

# Change all widget like interests 

class UserProfileNameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        # self.fields['first_name'].widget.attrs.update({'class': 'profile-input'})
        self.fields['last_name'].required = True

# And here like first_name