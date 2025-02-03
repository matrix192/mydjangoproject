from django.db import models

# Create your models here.
class Cars(models.Model):
    car_brand = models.CharField(max_length=30, null = False)
    car_model = models.CharField(max_length=30, null = False)
    car_type = models.CharField(max_length=20, null = False)
    engine_volume = models.FloatField(null=False)
    description = models.TextField(null = True, default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(null = False)
    published = models.DateTimeField(auto_now_add=True)
    price = models.TextField(null = False, default="Договорная")