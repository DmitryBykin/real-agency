# Generated by Django 2.2.4 on 2019-10-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_who_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_phone_pure',
            field=models.CharField(blank=True, max_length=20, verbose_name='Нормализованный номер владельца'),
        ),
    ]
