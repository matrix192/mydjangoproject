from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Make(models.Model):
    name = models.CharField(
    max_length=100, 
    verbose_name='Марка', 
    unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Марка транспорта'
        verbose_name_plural = 'Марки автомобилей'
        ordering = ['name']

class Model(models.Model):
    name = models.CharField(max_length=100, verbose_name='Модель')
    make = models.ForeignKey(
        Make,
        on_delete=models.CASCADE, 
        related_name='models', 
        verbose_name='Марка')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ('name', 'make')
        verbose_name = 'Модель транспорта'
        verbose_name_plural = 'Модели транспорта'
        ordering = ['name']



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
    fuel = (
        ('b', 'Бензин'),
        ('d', 'Дизель'),
        ('g', 'Газ'),
        ('e', 'Электричка'),
    )
    kuzov = (
        ('1', 'Седан'),
        ('2', 'Универсал'),
        ('3', 'Хетчбек'),
        ('4', 'Купе'),
        ('5', 'Лимузин'),
        ('6', 'Микроавтобус'),
        ('7', 'Минивэн'),
        ('8', 'Хардтоп'),
        ('9', 'Таун-кар'),
        ('a', 'Комби'),
        ('b', 'Лифтбек'),
        ('c', 'Фастбек'),
        ('d', 'Кабриолет'),
        ('e', 'Пикап'),
        ('f', 'Фургон'),
    )

    make = models.ForeignKey(
        Make, 
        on_delete=models.CASCADE, 
        max_length=30, 
        null = False, 
        blank = True, 
        verbose_name="Марка автомобиля")
    model = models.ForeignKey(
        Model, 
        on_delete=models.CASCADE, 
        max_length=30, 
        null = False, 
        blank = True, 
        verbose_name="Модель авто")
    car_type = models.CharField(
        max_length=1, 
        choices=kuzov, 
        null = False, 
        blank = True, 
        verbose_name="Тип кузова")
    engine_volume = models.FloatField(
        null=False, 
        blank = True, 
        verbose_name="Объем двигателя")
    description = models.TextField(
        null = True, 
        blank = True, 
        verbose_name="Описание автомобиля", 
        default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(
        null = False, 
        blank = True, 
        verbose_name="Год выпуска")
    published = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата публикации объявления")
    price = models.FloatField(
        null = False, 
        blank = True, 
        verbose_name="Цена")
    condition = models.CharField(
        max_length=1, 
        choices=conditions, 
        default='s', 
        verbose_name="Состояние")
    transmission_box = models.CharField(
        max_length=1, 
        choices=box_type, 
        default = "m", 
        verbose_name="Коробка передач")
    color = models.CharField(
        max_length=20, 
        null=False, 
        blank=True, 
        verbose_name="Цвет авто")
    fuel_type = models.CharField(
        max_length=1, 
        choices=fuel, 
        verbose_name="Тип топлива")
    Mileage = models.IntegerField(
        null=False, 
        blank=True, 
        verbose_name='Пробег')

    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return f'{self.make} {self.model} {str(self.year_of_release)}'
    
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
    gear = (
        ('c', 'Цепь'),
        ('k', 'Кардан'),
        ('r', 'Ремень'),
    ) 

    make = models.ForeignKey(
        Make, 
        on_delete=models.CASCADE, 
        max_length=30, 
        null = False, 
        blank = True, 
        verbose_name="Марка автомобиля")
    model = models.ForeignKey(
        Model, 
        on_delete=models.CASCADE, 
        max_length=30, 
        null = False, 
        blank = True, 
        verbose_name="Модель авто")
    engine_volume = models.FloatField(
        null=False, 
        blank = True, 
        verbose_name="Объем двигателя в см^3")
    description = models.TextField(
        null = True, 
        blank = True, 
        verbose_name="Описание транспорта", 
        default="Напишите продавцу и узнайте подробности!")
    year_of_release = models.IntegerField(
        null = False, 
        blank = True, 
        verbose_name="Год выпуска")
    published = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата опубликования объявления")
    price = models.FloatField(
        null = False, 
        blank = True, 
        verbose_name="Цена")
    condition = models.CharField(
        max_length=1, 
        choices=conditions, 
        default='s', 
        verbose_name="Состояние")
    main_gear = models.CharField(
        max_length=1, 
        choices=gear, 
        null=False, 
        blank=True, 
        verbose_name='Главная передача')
    color = models.CharField(
        max_length=20, 
        null=False, 
        blank=True, 
        verbose_name="Цвет транспорта")
    Mileage = models.IntegerField(
        null=False, 
        blank=True, 
        verbose_name='Пробег', default=0)


    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
      return f"{self.make} {self.model} {str(self.engine_volume)}"

    class Meta:
        verbose_name_plural = 'Мотоциклы'
        verbose_name = 'Мотоцикл'
        ordering = ['-published']

class Profile(models.Model):
    is_active = models.BooleanField(default=False)
    is_seller = models.BooleanField(
        default=False, 
        verbose_name="Продавец?")
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'