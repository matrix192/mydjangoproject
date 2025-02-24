from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Cars, Moto

def index_page(request):
    return render(request, "buycars/index.html")

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

def car_detail(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'buycars/details_car.html', {'car': car})

def moto_detail(request, id):
    moto = get_object_or_404(Moto, id=id)
    return render(request, 'buycars/details_moto.html', {'moto': moto})

