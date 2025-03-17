from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from buycars.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'is_seller']

