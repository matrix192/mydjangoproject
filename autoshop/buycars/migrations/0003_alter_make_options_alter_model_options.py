# Generated by Django 5.1.5 on 2025-03-16 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buycars', '0002_moto_mileage_alter_cars_car_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='make',
            options={'ordering': ['name'], 'verbose_name': 'Марка транспорта', 'verbose_name_plural': 'Марки автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'ordering': ['name'], 'verbose_name': 'Модель транспорта', 'verbose_name_plural': 'Модели транспорта'},
        ),
    ]
