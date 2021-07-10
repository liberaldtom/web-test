
from django.urls import path
from . import views

#Paths core
urlpatterns = [
    path('services/', views.services, name="services"),
]