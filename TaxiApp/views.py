from .models import Vehicles
from django.shortcuts import render

def index(request):
 vehicles = Vehicles.objects.order_by('-issueYear')
 return render(request, "TaxiApp/index.html", {'vehicles': vehicles})