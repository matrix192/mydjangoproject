from django.urls import path
from buycars.views import *

app_name = 'buycars'
urlpatterns = [
    path('', index_page, name = 'index_page'),
    path('moto/', two_wheels, name = 'two_wheels'),
    path('cars/', car_list, name = 'car_list'),
    path('cars/<int:id>/', car_detail, name='car_detail'),
    path('moto/<int:id>/', moto_detail, name='moto_detail'),
    path('cars/sorted/', sortirovka_cars, name='sortirovka_cars'),
    path('moto/sorted/', sortirovka_moto, name='sortirovka_moto')
]