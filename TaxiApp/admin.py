from django.contrib import admin
from .models import Vehicles
from .models import Level
from .models import Driver
from .models import Order
class VehiclesAdmin(admin.ModelAdmin):
 list_display = ('mark', 'gosNumber', 'color', 'issueYear', 'level')
 list_display_links = ('mark', 'gosNumber')
 search_fields = ('mark', 'gosNumber', 'color', 'issueYear', 'level')

class DriverAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'lastName', 'birthDate', 'inn', 'serno', 'vehicle')
    list_display_links = ('surname', 'vehicle')
    search_fields = ('surname', 'name', 'lastName', 'birthDate', 'inn', 'serno', 'vehicle')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateTime', 'departure', 'destination', 'passangerNumber', 'length', 'driver')
    list_display_links = ('id', 'dateTime')
    search_fields = ('id', 'dateTime', 'departure', 'destination', 'passangerNumber', 'length', 'driver')

admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Level)
