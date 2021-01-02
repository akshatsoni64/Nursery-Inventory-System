from django.shortcuts import render, redirect
from django.views import View
from django.http import *
from .forms import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers

# Do not remove this key(Encryption for plant_id)
key = 4

class PlantViews(LoginRequiredMixin, APIView):
    login_url = '/login'
    def get(self, request, id=None):
        context = {}
        usr = User.objects.get(username = request.user)
        cust = Customer.objects.get(user = usr)
        context['user_type'] = cust.type
        # if not request.user.is_authenticated:
        #     return redirect('/login')
        # else:
        if id is not None:
            plant = Plant.objects.get(id = id)
            serializer = PlantSerializers(plant, many = False)
            context['info'] = serializer.data
            context['plant_id'] = id + key
            context['form'] = OrderForm()
            return render(request, 'display.html', context)
            # return Response(serializer.data)
        else:
            print(request.user)

        form = PlantForm()
        plants = Plant.objects.all()
        serializer = PlantSerializers(plants, many=True)

        context['form'] = PlantForm()
        context['plants'] = serializer.data

        return render(request, "index.html", context)


    def post(self, request, id=None):
        form = PlantForm(request.POST or None, request.FILES or None)
        context = {}
        usr = User.objects.get(username = request.user)
        cust = Customer.objects.get(user = usr)
        context['user_type'] = cust.type
        context['form'] = PlantForm()
        valid = form.is_valid()
        print(valid)
        print("\n", request.FILES)
        if valid:
            form.save()
            context['status'] = "success"
            # return JsonResponse(request.POST)            
        else:
            context['error'] = form.errors
            # return JsonResponse(form.errors)
        
        plants = Plant.objects.all()
        serializer = PlantSerializers(plants, many=True)
        context['plants'] = serializer.data
        return render(request, 'index.html', context)

class OrderViews(LoginRequiredMixin, APIView):
    login_url = '/login'
    def get(self, request):
        form = OrderForm()        
        context = {"form": form}
        usr = User.objects.get(username = request.user)
        cust = Customer.objects.get(user = usr)
        if cust.type == "customer":
            orders = Order.objects.filter(cust=cust)
        else:
            orders = Order.objects.all()
        context['orders'] = orders
        context['user_type'] = cust.type
        return render(request, 'orders.html', context)

    def post(self, request):
        context = {}
        
        id = int(request.POST['plant_id']) - key
        plant = Plant.objects.get(id = id)
        
        quantity = int(request.POST['quantity'])
        usr = User.objects.get(username=request.user)
        cust = Customer.objects.get(user=usr)
        
        order = Order(plant=plant, cust=cust, quantity=quantity, price=(quantity*plant.price))
        order.save()
        if cust.type == "customer":
            orders = Order.objects.filter(cust=cust)
        else:
            orders = Order.objects.all()
        context['orders'] = orders
        context['user_type'] = cust.type        
        return render(request, 'orders.html', context)

    def delete(self, request):
        pass

class CustomerViews(APIView):
    def get(self, request):
        custForm = CustomerForm()
        context = {"custForm": custForm}
        return render(request, 'register.html', context)

    def post(self, request):        
        # return JsonResponse(userForm)
        # return render(request, 'register.html', context)
        custForm = CustomerForm(request.POST)
        print(custForm.is_valid())
        context = {"custForm": custForm}
        if custForm.is_valid():
            cust = custForm.save()
            cust.refresh_from_db()
            cust.customer.mobile = custForm.cleaned_data.get('mobile')
            cust.customer.address = custForm.cleaned_data.get('address')
            cust.customer.type = custForm.cleaned_data.get('type')
            cust.save()
            context['success'] = "You may login now"
        else:
            context = {"custForm": CustomerForm(), "error": custForm.errors}            
        return render(request, 'register.html', context)

"""
akshat
This_6464
"""
class AuthViews(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/p')
        
        form = LoginForm()
        context = {"form": form}
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        context = {}
        print("User: ", user)
        if user is not None:
            auth.login(request, user)
            return redirect('/p')
        else:
            context['status'] = "Error"
            context['form'] = LoginForm()
            return render(request, 'login.html', context)

def logout_view(request):
    auth.logout(request)
    print(request.user)
    return redirect('/login')