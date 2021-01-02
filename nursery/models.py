from django.db.models import *
from django.core.validators import *
from django.contrib.auth.models import User

class Customer(Model):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        primary_key=True
    )
    mobile = BigIntegerField(validators=[MinValueValidator(1111111111)], null=True)
    address = TextField(max_length=200, null=True) 
    type = CharField(
        max_length=30, 
        choices=[
            ('customer', 'customer'),
            ('nursery', 'nursery')
        ],
        default='customer'
    )

class Plant(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=30)
    stock = IntegerField(validators=[MinValueValidator(1)])
    price = IntegerField(validators=[MinValueValidator(1)])
    image = ImageField(upload_to="static/", default="static/default.jpg")

class Order(Model):
    id = AutoField(primary_key=True)
    plant = ForeignKey(Plant, on_delete=SET_NULL, null=True)
    cust = ForeignKey(Customer, on_delete=SET_NULL, null=True)
    quantity = IntegerField(validators=[MinValueValidator(1)])
    price = IntegerField(validators=[MinValueValidator(1)])
