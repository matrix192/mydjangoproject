from django.db import models

# Create your models here.
class Cars(models.Model):
    car_brand = models.CharField(max_length=30, null = False, blank = True, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=30, null = False, blank = True, verbose_name="Модель автомобиля")
    car_type = models.CharField(max_length=20, null = False, blank = True, verbose_name="Тип кузова")
    engine_volume = models.FloatField(null=False, blank = True, verbose_name="Объем двигателя")
    description = models.TextField(null = True, blank = True, verbose_name="Описание автомобиля", default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(null = False, blank = True, verbose_name="Год выпуска")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования объявления")
    price = models.TextField(null = False, blank = True, default="Договорная", verbose_name="Цена")
    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return self.car_brand + " " + self.car_model + " " + str(self.year_of_release)
    
    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-published']

class Moto(models.Model):
    moto_brand = models.CharField(max_length=30, null = False, blank = True, verbose_name="Марка мотоцикла")
    moto_model = models.CharField(max_length=30, null = False, blank = True, verbose_name="Модель мотоцикла")
    engine_volume = models.FloatField(null=False, blank = True, verbose_name="Объем двигателя в см^3")
    description = models.TextField(null = True, blank = True, verbose_name="Описание транспорта", default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(null = False, blank = True, verbose_name="Год выпуска")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования объявления")
    price = models.TextField(null = False, blank = True, default="Договорная", verbose_name="Цена")
    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return self.moto_brand + " " + self.moto_model + " " + str(self.engine_volume)

    class Meta:
        verbose_name_plural = 'Мотоциклы'
        verbose_name = 'Мотоцикл'
        ordering = ['-published']