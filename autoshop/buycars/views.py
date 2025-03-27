from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Cars, Moto
from .forms import SignUpForm, CarAdForm

def index_page(request):
    return render(request, "buycars/index.html")

def car_list(request):
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


def two_wheels(request):
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


def car_detail(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'buycars/details_car.html', {'car': car})

def moto_detail(request, id):
    moto = get_object_or_404(Moto, id=id)
    return render(request, 'buycars/details_moto.html', {'moto': moto})

def custom_page_not_found(request, exception):
    return render(request, 'buycars/404.html', status=404)


@login_required
def add_car_ad(request):
    if not request.user.profile.is_seller:
        return redirect('index_page')  # Перенаправляем, если пользователь не продавец
    if request.method == 'POST':
        form = CarAdForm(request.POST)
        if form.is_valid():
            car_ad = form.save(commit=False)
            car_ad.seller = request.user
            car_ad.save()
            return redirect('index_page')
    else:
        form = CarAdForm()
    return render(request, 'add_car_ad.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_page')  # Перенаправление после успешной регистрации
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})