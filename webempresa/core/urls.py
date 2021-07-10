
from django.urls import path
from core import views

urlpatterns = [

#Paths core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.about, name="store"),
]


