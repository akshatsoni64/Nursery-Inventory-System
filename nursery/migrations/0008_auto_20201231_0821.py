# Generated by Django 3.1.4 on 2020-12-31 08:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0007_auto_20201230_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='mobile',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1111111111)]),
        ),
    ]
