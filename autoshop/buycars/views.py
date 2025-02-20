from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cars, Moto

def index_page(request):
    return render(request, "buycars\index.html")

def car_list(request):
    template = loader.get_template('buycars/cars.html')
    vehicles = Cars.objects.order_by("-published")
    context = {"vehicles" : vehicles}
    return HttpResponse(template.render(context, request))

def two_wheels(request):
    template = loader.get_template('buycars/moto.html')
    half_car = Moto.objects.order_by("-published")
    context = {"half_car" : half_car}
    return HttpResponse(template.render(context, request))

