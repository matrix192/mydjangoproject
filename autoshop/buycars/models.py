from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.conf import settings
# Create your models here.


# class Make(models.Model):
#     name = models.CharField(
#         max_length=100, 
#         verbose_name='Марка', 
#         unique=True
#     )

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Марка транспорта'
#         verbose_name_plural = 'Марки автомобилей'
#         ordering = ['name']


# class Model(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Модель')
#     make = models.ForeignKey(
#         'Make',
#         on_delete=models.CASCADE,  # Разрешено каскадное удаление
#         related_name='models', 
#         verbose_name='Марка'
#     )

#     def __str__(self):
#         return f"{self.name}"

#     class Meta:
#         unique_together = ('name', 'make')
#         verbose_name = 'Модель транспорта'
#         verbose_name_plural = 'Модели транспорта'
#         ordering = ['name']
alphanumeric_validator = RegexValidator(
    r'^[a-zA-Zа-яА-ЯёЁ\s-]*$',
    'Разрешены только буквы, пробел и дефис'
)

russian_validator = RegexValidator(
    r'^[а-яА-ЯёЁ-]*$',
    'Разрешена только кириллица и дефис'
)


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
        ('g', 'Внедорожник')
    )

    make = models.CharField(
        max_length=40, 
        null=False, 
        blank=True, 
        verbose_name="Марка автомобиля",
        validators=[alphanumeric_validator],
    )
    model = models.CharField(
        max_length=30, 
        null=False, 
        blank=True, 
        verbose_name="Модель авто"
    )
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
        verbose_name="Описание автомобиля",)
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
        verbose_name="Состояние")
    transmission_box = models.CharField(
        max_length=1, 
        choices=box_type, 
        verbose_name="Коробка передач")
    color = models.CharField(
        max_length=20, 
        validators=[russian_validator],
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
        return f'{self.make} {self.model} {str(self.year_of_release)}'
    
    def clean(self):
        if self.year_of_release < 1900 or self.year_of_release > 2025:
            raise ValidationError({'year_of_release':"Проверьте правильность ввода даты выпуска автомобиля!"})
        
        if self.Mileage < 0:
            raise ValidationError({'Mileage':"Проверьте правильность ввода пробега автомобиля!"})
        
        if self.price < 0:
            raise ValidationError({'price':"Проверьте правильность ввода цены на авто!"})
        
        if self.engine_volume > 9 or self.engine_volume < 0:
            raise ValidationError({'engine_volume':"Проверьте правильность ввода объема двигателя!"})
    
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

    make = models.CharField(
        max_length=30, 
        null=False, 
        validators=[alphanumeric_validator],
        blank=True, 
        verbose_name="Марка мотоцикла"
    )
    model = models.CharField(
        max_length=30, 
        null=False, 
        blank=True, 
        verbose_name="Модель"
    )    
    engine_volume = models.FloatField(
        null=False, 
        blank = True, 
        verbose_name="Объем двигателя в см^3")
    description = models.TextField(
        null = True, 
        blank = True, 
        verbose_name="Описание транспорта",)
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
        validators=[russian_validator],
        blank=True, 
        verbose_name="Цвет транспорта")
    Mileage = models.IntegerField(
        null=False, 
        blank=True, 
        verbose_name='Пробег',)


    # image = models.ImageField(null = False, blank = True)

    def __str__(self):
      return f"{self.make} {self.model} {str(self.engine_volume)}"

    class Meta:
        verbose_name_plural = 'Мотоциклы'
        verbose_name = 'Мотоцикл'
        ordering = ['-published']

class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True)
    is_seller = models.BooleanField(default=False, verbose_name='Продавец?')

    def clean(self):
        if not self.phone.startswith('+375'):
            raise ValidationError('Номер должен начинаться с "+375" (Беларусь)')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    car = models.ForeignKey(
        'Cars',
        on_delete=models.CASCADE,
        verbose_name="Автомобиль"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        unique_together = ('user', 'car')
        verbose_name = 'Список избранных автомобилей'
        verbose_name_plural = 'Избранные авто'

    def __str__(self):
        return f"{self.user.username} - {self.car}"
    
class Favorite_moto(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    moto = models.ForeignKey(
        'Moto',
        on_delete=models.CASCADE,
        verbose_name="Мотоцикл"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        unique_together = ('user', 'moto')
        verbose_name = 'Список избранных мотоциклов'
        verbose_name_plural = 'Избранные мотоциклы'

    def __str__(self):
        return f"{self.user.username} - {self.moto}"