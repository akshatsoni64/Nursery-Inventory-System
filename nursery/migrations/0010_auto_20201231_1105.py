# Generated by Django 3.1.4 on 2020-12-31 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0009_auto_20201231_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='cust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nursery.customermodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nursery.plantmodel'),
        ),
    ]
