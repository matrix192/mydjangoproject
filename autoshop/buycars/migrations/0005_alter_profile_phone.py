# Generated by Django 5.1.5 on 2025-03-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycars', '0004_alter_profile_managers_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='null', max_length=15, unique=True, verbose_name='Номер телефона'),
        ),
    ]
