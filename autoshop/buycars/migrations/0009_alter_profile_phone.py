# Generated by Django 5.1.5 on 2025-04-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycars', '0008_favorite_moto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='null', max_length=15, verbose_name='Номер телефона'),
        ),
    ]
