from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cars

def index_page(request):
    # return HttpResponse("Тут будет первая страница!")
    template = loader.get_template('buycars/index.html')
    Vehicles = Cars.objects.order_by("-published")
    context = {"cars" : Vehicles}
    return HttpResponse(template.render(context, request))

# Create your views here.
