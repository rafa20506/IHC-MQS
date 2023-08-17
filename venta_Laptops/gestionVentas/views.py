
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from gestionVentas.models import Producto

from gestionVentas.models import Producto,Venta

from .forms import FormularioAgregarPrd

from django.contrib.auth import authenticate
from gestionVentas.models import Usuario

from collections import Counter

from django.contrib.messages import constants as messages

import sweetify




def search(request):
    if request.GET["busqueda"]:
        print(request.GET["busqueda"])
        produc = request.GET["busqueda"]
    articulos = Producto.objects.get(marca__icontains=produc)
    n=3
    print(request.GET["busqueda"])
    productos1=[articulos[i:i + n] for i in range(0, len(articulos), n)]
    return render(request, "gestionVentas/search.html",{"productos": productos1})

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

def landing(request):

    return render(request, "gestionVentas/landing.html")
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
    ventas=Venta.objects.all()
    serials=[]
    for venta in ventas:
        serials.append(venta.vSerialNumber)
    counter = Counter(serials)
    first, second,threeth,fourth,fifth, *_, last = counter.most_common()
    tendencias=[]
    prodcutTendencia=Producto.objects.get(serialNumber__icontains=first[0])
    tendencias.append(prodcutTendencia)
    prodcutTendencia=Producto.objects.get(serialNumber__icontains=second[0])
    tendencias.append(prodcutTendencia)
    prodcutTendencia=Producto.objects.get(serialNumber__icontains=threeth[0])
    tendencias.append(prodcutTendencia)
    prodcutTendencia=Producto.objects.get(serialNumber__icontains=fourth[0])
    tendencias.append(prodcutTendencia)
    prodcutTendencia=Producto.objects.get(serialNumber__icontains=fifth[0])
    tendencias.append(prodcutTendencia)
    
    print(first[0])

    for tendencia in tendencias:
        print(tendencia.marca)
    
    productos0 = Producto.objects.all()

    
    n=3

    productos1=[productos0[i:i + n] for i in range(0, len(productos0), n)]
    return render(request, "gestionVentas/prueba.html", {"productos1":productos1,"tendencias":tendencias})


def addProducto(request):
    formulario_prodcuto = FormularioAgregarPrd()
    return render(request, "gestionVentas/agregar.html",{'miFormulario': formulario_prodcuto})
  
def search2(request):
    print(request.GET["fname"])
    if "fname" in request.GET:
        
    
        print(request.GET["fname"]+"entro")
        productos = Producto.objects.all()
        #return render(request, "gestionVentas/login.html", {"productos":productos})
        produc = request.GET["fname"]
        #mensaje = "el articulo: %r " %request.GET["prd"] #saca el elemento del campo de buscar del html
        articulos2 = Producto.objects.filter(marca__icontains=produc)
        n=3

        articulos=[articulos2[i:i + n] for i in range(0, len(articulos2), n)]
        return render(request, "gestionVentas/search2.html", {"articulos": articulos, "query":produc})

    else:
        
        return render(request, "gestionVentas/prueba.html")

def verificar(request):
    if "correo" in request.GET and "contrasenia" in request.GET:
        correo = request.GET["correo"]
        contraseniaa  = request.GET["contrasenia"]
        
        usuario = Usuario.objects.filter(correo=correo)
        if usuario.exists():
            # Aquí puedes realizar la verificación de la contraseña de manera segura
            if usuario[0].contrasenia == contraseniaa:
                #return HttpResponseRedirect("{% url 'Prueba' %}")  # Redireccionar a otra página
                return render(request, "gestionVentas/laptops.html")
            else:
               print("contraseña incorrecta")
               
                
        else:
            print("Usuario no encontrado")
    else:
        print("Parámetros faltantes")
    
    return render(request, "gestionVentas/login.html")

def cerrarSesion(request):
    return render(request, "gestionVentas/landing.html")
