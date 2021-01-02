# Generated by Django 3.1.4 on 2020-12-30 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0003_auto_20201230_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(1111111111)])),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]