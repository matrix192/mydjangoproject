from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Cars, Moto
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    is_seller = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2', 'email', 'phone', 'is_seller')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.is_seller = self.cleaned_data['is_seller']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  # Не создаём отдельный Profile, потому что user ЭТО И ЕСТЬ Profile!
    
class CarAdForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['make', 
                  'model', 
                  'year_of_release', 
                  'price', 
                  'description', 
                  'engine_volume', 
                  'car_type', 
                  'condition', 
                  'transmission_box', 
                  'color', 
                  'fuel_type', 
                  'Mileage',
                  ]
        
class MotoAdForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['make', 
                  'model', 
                  'engine_volume', 
                  'price', 
                  'year_of_release',
                  'description',
                  'condition',
                  'color',
                  'main_gear',
                  'Mileage',
                  ]