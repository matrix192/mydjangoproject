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
    # return render(request, "buycars/cars.html")

def two_wheels(request):
    template = loader.get_template('buycars/moto.html')
    half_car = Moto.objects.all()
    context = {"half_car" : half_car}
    return HttpResponse(template.render(context, request))

def car_detail(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'buycars/details_car.html', {'car': car})

def moto_detail(request, id):
    moto = get_object_or_404(Moto, id=id)
    return render(request, 'buycars/details_moto.html', {'moto': moto})

def sortirovka_cars(request):
    queryset = Cars.objects.all()

    sort_by = request.GET.get('sort', '')

    if sort_by == 'date_asc':
        queryset = queryset.order_by('published')  
    elif sort_by == 'date_desc':
        queryset = queryset.order_by('-published')  
    elif sort_by == 'price_asc':
        queryset = queryset.order_by('price') 
    elif sort_by == 'price_desc':
        queryset = queryset.order_by('-price') 
    elif sort_by == 'name_asc':
        queryset = queryset.order_by('make', 'model') 
    elif sort_by == 'name_desc':
        queryset = queryset.order_by('-make', '-model')  

    context = {
        'vehicles': queryset,
    }
    return render(request, 'buycars/cars.html', context)

def sortirovka_moto(request):
    queryset = Moto.objects.all()

    sort_by = request.GET.get('sort', '')

    if sort_by == 'date_asc':
        queryset = queryset.order_by('published')  
    elif sort_by == 'date_desc':
        queryset = queryset.order_by('-published')  
    elif sort_by == 'price_asc':
        queryset = queryset.order_by('price') 
    elif sort_by == 'price_desc':
        queryset = queryset.order_by('-price') 
    elif sort_by == 'name_asc':
        queryset = queryset.order_by('make', 'model') 
    elif sort_by == 'name_desc':
        queryset = queryset.order_by('-make', '-model')  

    context = {
        'half_car': queryset
    }
    return render(request, 'buycars/moto.html', context)
