from django.contrib import admin
from .models import Cars, Moto, Profile, Make, Model

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_seller')
@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'price')
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'price')
admin.site.register(Make)
admin.site.register(Model)
