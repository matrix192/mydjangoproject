from django.contrib import admin
from .models import Cars, Moto, Profile, Make, Model

admin.site.register(Profile)
admin.site.register(Moto)
admin.site.register(Cars)
admin.site.register(Make)
admin.site.register(Model)
