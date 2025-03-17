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
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))