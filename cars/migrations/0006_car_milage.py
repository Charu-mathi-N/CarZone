# Generated by Django 3.2.4 on 2021-06-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_rename_feul_type_car_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='milage',
            field=models.IntegerField(default=27),
            preserve_default=False,
        ),
    ]
