from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, Paginator
# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,


    }
    return render(request, "cars/cars.html", data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car
    }
    # data = 10/0
    # raise ValueError('A very specific bad thing happened.')
    return render(request, "cars/car_details.html", data)

def search(request):
    car = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            car = car.filter(description__icontains=keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            car = car.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            car = car.filter(city__iexact=city)
    
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            car = car.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            car = car.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            car = car.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'car':car,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,


    }
    return render(request, "pages/search.html", data)