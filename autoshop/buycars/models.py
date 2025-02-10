from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cars(models.Model):
    conditions = (
      ('n', 'Новый'),
      ('s', 'Б/У'),
      ('p', 'На запчасти'),
    ) 

    box_type = (
      ('m', 'Механика'),
      ('a', 'Автомат'),
      ('r', 'Робот'),
    ) 

    car_brand = models.CharField(max_length=30, null = False, blank = True, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=30, null = False, blank = True, verbose_name="Модель автомобиля")
    car_type = models.CharField(max_length=20, null = False, blank = True, verbose_name="Тип кузова")
    engine_volume = models.FloatField(null=False, blank = True, verbose_name="Объем двигателя")
    description = models.TextField(null = True, blank = True, verbose_name="Описание автомобиля", default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(null = False, blank = True, verbose_name="Год выпуска")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования объявления")
    price = models.FloatField(null = False, blank = True, verbose_name="Цена")
    condition = models.CharField(max_length=1, choices=conditions, default='s', verbose_name="Состояние")
    transmission_box = models.CharField(max_length=1, choices=box_type, default = "m", verbose_name="Коробка передач")
    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return self.car_brand + " " + self.car_model + " " + str(self.year_of_release)
    
    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-published']

class Moto(models.Model):
    conditions = (
      ('n', 'Новый'),
      ('s', 'Б/У'),
      ('p', 'На запчасти'),
    ) 

    moto_brand = models.CharField(max_length=30, null = False, blank = True, verbose_name="Марка мотоцикла")
    moto_model = models.CharField(max_length=30, null = False, blank = True, verbose_name="Модель мотоцикла")
    engine_volume = models.FloatField(null=False, blank = True, verbose_name="Объем двигателя в см^3")
    description = models.TextField(null = True, blank = True, verbose_name="Описание транспорта", default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(null = False, blank = True, verbose_name="Год выпуска")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования объявления")
    price = models.FloatField(null = False, blank = True, verbose_name="Цена")
    condition = models.CharField(max_length=1, choices=conditions, default='s', verbose_name="Состояние")
    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return self.moto_brand + " " + self.moto_model + " " + str(self.engine_volume)

    class Meta:
        verbose_name_plural = 'Мотоциклы'
        verbose_name = 'Мотоцикл'
        ordering = ['-published']

class Profile(models.Model):
    is_active = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False, verbose_name="Продавец?")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'