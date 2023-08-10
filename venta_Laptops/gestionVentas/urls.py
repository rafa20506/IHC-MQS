## del proyecto
from django.urls import path
from gestionVentas import views

urlpatterns = [
    
    path('', views.ladingPage, name='LadingPage'),
    path('home', views.home, name="Home"),
    
]
