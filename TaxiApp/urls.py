from django.urls import path
from .views import index
from TaxiApp import views

urlpatterns = [
 path('', index),
]