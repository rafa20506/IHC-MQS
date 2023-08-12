## del proyecto
from django.urls import path
from gestionVentas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.landing, name='landing'),
    path('home', views.home, name="Home"),
    path('laptops',views.laptops, name="Laptops"),
    path('login', views.login, name="login"),
    path('homepi', views.homepi, name="Homepi"),
    path('prueba', views.prueba, name="Prueba"),
    path('agregar', views.agregar, name="Agregar"),
    path('agregarProducto', views.addProducto, name="AgregarProducto"),
    path('pruebaLogin', views.pruebaLogin, name= "PruebaLogin"),

    path('verificar', views.prueba, name="prueba"),# nombre de la direccion tiene que ser el mismo que en viwes
    path('search', views.search, name= "Search"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
