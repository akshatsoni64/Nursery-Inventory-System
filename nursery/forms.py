from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput()
    )

    class Meta:
        fields = '__all__'

class CustomerForm(UserCreationForm):
    mobile = forms.IntegerField()
    address = forms.CharField()
    type = forms.CharField(
        widget=forms.Select(choices=[
            ('customer', 'Customer'),
            ('nursery', 'Nursery')
        ])
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile', 'address', 'type')

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'stock', 'price', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']