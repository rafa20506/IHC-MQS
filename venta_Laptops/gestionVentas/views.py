
from django.http import HttpResponse
from django.shortcuts import render
from gestionVentas.models import Producto

from gestionVentas.models import Producto

from .forms import FormularioAgregarPrd

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

def pruebaLogin(request):
    mensaje ="contraseña: %r " %request.GET["correo"]
    return render(request,"inicio.html")
    #return HttpResponse(mensaje)

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
    productos = Producto.objects.all()
    return render(request, "gestionVentas/laptops.html", {"productos":productos})

def agregar(request):

    formulario_prodcuto = FormularioAgregarPrd()
    return render(request, "gestionVentas/agregar.html",{'miFormulario': formulario_prodcuto})
    #return render(request, "gestionVentas/agregar.html")

def homepi(request):
    return render(request, "gestionVentas/homepi.html")

def prueba(request):
    return render(request, "gestionVentas/prueba.html")


def addProducto(request):
    formulario_prodcuto = FormularioAgregarPrd()
    return render(request, "gestionVentas/agregar.html",{'miFormulario': formulario_prodcuto})

