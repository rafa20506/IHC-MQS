
from django.http import HttpResponse
from django.shortcuts import render
from gestionVentas.models import Producto
# Create your views here.
def busqueda_productos(request):

    return render(request, "busqueda_Producto.html")

def buscar(request):
    if request.GET["prd"]:
        produc = request.GET["prd"]
        #mensaje = "el articulo: %r " %request.GET["prd"] #saca el elemento del campo de buscar del html
        articulos = Producto.objects.filter(marca__icontains=produc)

        return render(request, "resultados_Busqueda.html", {"productos": articulos, "query":produc})
    else:
        mensaje = "No has introducido nada"
    return HttpResponse(mensaje)



def ladingPage(request):

    return render(request, "gestionVentas/ladingPage.html")
    #return HttpResponse("LadingPage")

def home(request):
    return render(request, "gestionVentas/home.html")
    #return HttpResponse("Home")

def login(request):
    return render(request, "gestionVentas/login.html")
    #return HttpResponse("Home")

def laptops(request):
    return render(request, "gestionVentas/laptops.html")

def homepi(request):
    return render(request, "gestionVentas/homepi.html")
