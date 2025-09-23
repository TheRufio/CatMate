from django import forms
from .models import UserProfile
from registration.models import CustomUser
from .choices import Gender

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'age', 'gender', 'interests']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'field-value avatar',
                                             'style': "display:none"}),
            'age': forms.NumberInput(attrs={'class': 'field-value'}),
            'gender': forms.Select(choices=Gender.choices,
                                   attrs={'class': 'select-gender'}),
            'interests': forms.CheckboxSelectMultiple(attrs={'class': 'field-value'}),
        } 

# Change all widget like interests 

class UserProfileNameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['first_name'].widget.attrs.update({'class': 'field-value'})
        self.fields['last_name'].required = True
        self.fields['last_name'].widget.attrs.update({'class': 'field-value'})

# And here like first_name