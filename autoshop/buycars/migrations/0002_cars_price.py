# Generated by Django 5.1.5 on 2025-02-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='price',
            field=models.TextField(default="Договорная"),
            preserve_default=False,
        ),
    ]
