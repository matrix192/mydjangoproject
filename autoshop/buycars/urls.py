from django.urls import path
from buycars.views import index_page, car_list, two_wheels

app_name = 'buycars'
urlpatterns = [
    path('', index_page, name = 'index_page'),
    path('moto/', two_wheels, name = 'two_wheels'),
    path('cars/', car_list, name = 'car_list'),
]

