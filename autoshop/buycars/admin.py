from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_seller')
@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'price')
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'price')
# admin.site.register(Make)
# @admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make')
    list_filter = ('make',)
admin.site.register(Favorite_moto)
admin.site.register(Favorite)