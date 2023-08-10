"""
URL configuration for venta_Laptops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from venta_Laptops.views import saludo, despedida,prueba
from gestionVentas import views

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('', include('gestionVentas.urls'))  # apuntamos a la url de gestion ventas o app
]




"""  path('saludo/', saludo),    #prueba
    path('despedida/<nombre>',despedida), #prueba
    path('prueba/', prueba), #prueba
    path('busqueda_producto/', views.busqueda_productos),
    path('buscar/', views.buscar),
    path('', views.ladingPage, name='LadingGage'),
    path('home', views.home, name="Home"),
    """