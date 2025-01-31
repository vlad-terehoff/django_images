from django import forms
from .models import UserImages


class UserImagesForm(forms.ModelForm):
    class Meta:
        model = UserImages
        fields = ['name', 'description', 'shooting_date', 'image', 'tags']
        widgets = {
            'shooting_date': forms.DateInput(attrs={'type': 'date'}),
        }


class UserImagesUpdateForm(forms.ModelForm):
    class Meta:
        model = UserImages
        fields = ['name', 'description', 'shooting_date', 'tags']
        widgets = {
            'shooting_date': forms.DateInput(attrs={'type': 'date'}),
            'id': forms.HiddenInput()
        }
