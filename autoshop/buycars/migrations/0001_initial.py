# Generated by Django 5.1.5 on 2025-04-14 15:08

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ\\s-]*$', 'Разрешены только буквы, пробел и дефис')], verbose_name='Марка мотоцикла')),
                ('model', models.CharField(blank=True, max_length=30, verbose_name='Модель')),
                ('engine_volume', models.FloatField(blank=True, verbose_name='Объем двигателя в см^3')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание транспорта')),
                ('year_of_release', models.IntegerField(blank=True, verbose_name='Год выпуска')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата опубликования объявления')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('condition', models.CharField(choices=[('n', 'Новый'), ('s', 'Б/У'), ('p', 'На запчасти')], max_length=1, verbose_name='Состояние')),
                ('main_gear', models.CharField(blank=True, choices=[('c', 'Цепь'), ('k', 'Кардан'), ('r', 'Ремень')], max_length=1, verbose_name='Главная передача')),
                ('color', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[а-яА-ЯёЁ-]*$', 'Разрешена только кириллица и дефис')], verbose_name='Цвет транспорта')),
                ('Mileage', models.IntegerField(blank=True, verbose_name='Пробег')),
            ],
            options={
                'verbose_name': 'Мотоцикл',
                'verbose_name_plural': 'Мотоциклы',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')),
                ('is_seller', models.BooleanField(default=False, verbose_name='Продавец?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ\\s-]*$', 'Разрешены только буквы, пробел и дефис')], verbose_name='Марка автомобиля')),
                ('model', models.CharField(blank=True, max_length=30, verbose_name='Модель авто')),
                ('car_type', models.CharField(blank=True, choices=[('1', 'Седан'), ('2', 'Универсал'), ('3', 'Хетчбек'), ('4', 'Купе'), ('5', 'Лимузин'), ('6', 'Микроавтобус'), ('7', 'Минивэн'), ('8', 'Хардтоп'), ('9', 'Таун-кар'), ('a', 'Комби'), ('b', 'Лифтбек'), ('c', 'Фастбек'), ('d', 'Кабриолет'), ('e', 'Пикап'), ('f', 'Фургон')], max_length=1, verbose_name='Тип кузова')),
                ('engine_volume', models.FloatField(blank=True, verbose_name='Объем двигателя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание автомобиля')),
                ('year_of_release', models.IntegerField(blank=True, verbose_name='Год выпуска')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации объявления')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('condition', models.CharField(choices=[('n', 'Новый'), ('s', 'Б/У'), ('p', 'На запчасти')], max_length=1, verbose_name='Состояние')),
                ('transmission_box', models.CharField(choices=[('m', 'Механика'), ('a', 'Автомат'), ('r', 'Робот')], max_length=1, verbose_name='Коробка передач')),
                ('color', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[а-яА-ЯёЁ-]*$', 'Разрешена только кириллица и дефис')], verbose_name='Цвет авто')),
                ('fuel_type', models.CharField(choices=[('b', 'Бензин'), ('d', 'Дизель'), ('g', 'Газ'), ('e', 'Электричка')], max_length=1, verbose_name='Тип топлива')),
                ('Mileage', models.IntegerField(blank=True, verbose_name='Пробег')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buycars.cars', verbose_name='Автомобиль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Список избранных автомобилей',
                'verbose_name_plural': 'Избранные авто',
                'unique_together': {('user', 'car')},
            },
        ),
        migrations.CreateModel(
            name='Favorite_moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buycars.moto', verbose_name='Мотоцикл')),
            ],
            options={
                'verbose_name': 'Список избранных мотоциклов',
                'verbose_name_plural': 'Избранные мотоциклы',
                'unique_together': {('user', 'moto')},
            },
        ),
    ]
