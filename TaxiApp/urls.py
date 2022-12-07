from django.urls import path
from .views import index
from TaxiApp import views

urlpatterns = [
   path('', views.index, name='home'),
   path("vehicles", views.vehicles_page, name='vehicles'),
   path("driver", views.driver_page, name='driver'),
   path("order", views.order_page, name='order'),
]