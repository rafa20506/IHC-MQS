## del proyecto
from django.urls import path
from gestionVentas import views

urlpatterns = [
    
    path('', views.ladingPage, name='LadingPage'),
    path('home', views.home, name="Home"),
    path('laptops',views.laptops, name="Laptops"),
    path('login', views.login, name="Login"),
    path('homepi', views.homepi, name="Homepi"),
    
]
