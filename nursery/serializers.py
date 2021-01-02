from rest_framework.serializers import *
from .models import *

class PlantSerializers(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'