# Generated by Django 3.1.4 on 2020-12-30 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0006_auto_20201230_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='cust_id',
            new_name='cust',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='plant_id',
            new_name='plant',
        ),
    ]
