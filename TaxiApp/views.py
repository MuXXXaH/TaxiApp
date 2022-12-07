from .models import Vehicles
from django.shortcuts import render

def index(request):
 vehicles = Vehicles.objects.all()
 return render(request, "TaxiApp/index.html", {'vehicles': vehicles})