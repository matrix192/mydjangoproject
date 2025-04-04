from django.urls import path
from buycars.views import *
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache


app_name = 'buycars'
urlpatterns = [
    path('', index_page, name = 'index_page'),
    path('moto/', two_wheels, name = 'two_wheels'),
    path('cars/', car_list, name = 'car_list'),
    path('cars/<int:id>/', car_detail, name='car_detail'),
    path('moto/<int:id>/', moto_detail, name='moto_detail'),
    path('add-car-ad/', add_car_ad, name='add_car_ad'),
    path('favorite/<int:car_id>/', toggle_favorite_c, name='toggle_favorite_c'),
    path('favorite/<int:moto_id>/', toggle_favorite_m, name='toggle_favorite_m'),
    path('favorites_cars/', favorite_list_cars, name='favorite_list_cars'),
    path('favorites_moto/', favorite_list_moto, name='favorite_list_moto'),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))