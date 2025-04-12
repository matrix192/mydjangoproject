# Generated by Django 5.1.5 on 2025-04-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='condition',
            field=models.CharField(choices=[('n', 'Новый'), ('s', 'Б/У'), ('p', 'На запчасти')], max_length=1, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание автомобиля'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='transmission_box',
            field=models.CharField(choices=[('m', 'Механика'), ('a', 'Автомат'), ('r', 'Робот')], max_length=1, verbose_name='Коробка передач'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='Mileage',
            field=models.IntegerField(blank=True, verbose_name='Пробег'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='condition',
            field=models.CharField(choices=[('n', 'Новый'), ('s', 'Б/У'), ('p', 'На запчасти')], max_length=1, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание транспорта'),
        ),
    ]
