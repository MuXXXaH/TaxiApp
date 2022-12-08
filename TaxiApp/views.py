from .models import Vehicles, Driver, Order
from django.shortcuts import render

def index(request):
    return render(request, 'TaxiApp/index.html')


def vehicles_page(request):
    vehicles_items = Vehicles.objects.order_by('gosNumber')
    return render(request, 'TaxiApp/vehicles.html', {'vehicles_items': vehicles_items})


def driver_page(request):
    driver_items = Driver.objects.order_by('surname')
    return render(request, 'TaxiApp/driver.html', {'driver_items': driver_items})


def order_page(request):
    order_items = Order.objects.order_by('id')
    return render(request, 'TaxiApp/order.html', {'order_items': order_items})