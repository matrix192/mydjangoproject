from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Cars, Moto
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True, help_text='Номер телефона')
    is_seller = forms.BooleanField(required=False, help_text='Да-да, я продавец')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'is_seller', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(  # TODO: отображение юзернейма и почты в профиле пользователя
                user=user,
                phone=self.cleaned_data['phone'],
                is_seller=self.cleaned_data['is_seller']
            )
        return user
    

class CarAdForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['make', 
                  'model', 
                  'year_of_release', 
                  'description',
                  'car_type',
                  'engine_volume',
                  'condition',
                  'transmission_box',
                  'color',
                  'fuel_type',
                  'Mileage',
                  'price',
                  ]
        
class MotoAdForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['make', 
                  'model', 
                  'engine_volume', 
                  'description',
                  'year_of_release',
                  'main_gear',
                  'condition',
                  'color',
                  'Mileage',
                  'price', 
                  ]