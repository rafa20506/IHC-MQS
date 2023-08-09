from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    documento = open("../venta_Laptops/venta_Laptops/vistas/index2.html")   # la direccion relativa de los archivos html, css "vistas"
    
    plt = Template(documento.read())  #copiar siempre
    documento.close()               #copiar siempre

    ctx = Context()                 #copiar siempre
    documentoMostrar = plt.render(ctx) #copiar siempre

    return HttpResponse(documentoMostrar)  # el elemento que mostrara la paguina o web


def prueba(request):
    documento = open("../venta_Laptops/venta_Laptops/vistas/front2.html")   # la direccion relativa de los archivos html, css "vistas"
    
    plt = Template(documento.read())  #copiar siempre
    documento.close()               #copiar siempre

    ctx = Context()                 #copiar siempre
    documentoMostrar = plt.render(ctx) #copiar siempre

    return HttpResponse(documentoMostrar)  # el elemento que mostrara la paguina o web




def despedida(request, nombre):   # lo mismo de arriba pero con parametros
    documento = open("../venta_Laptops/venta_Laptops/vistas/index.html")   # la direccion relativa de los archivos html, css "vistas"
    
    plt = Template(documento.read())  #copiar siempre
    documento.close()               #copiar siempre

    ctx = Context({"nombre":nombre})     # aqui se modifica el apso de parametros   (tambien modificar el html)         #copiar siempre
    documentoMostrar = plt.render(ctx) #     #copiar siempre 

    return HttpResponse(documentoMostrar)  # el elemento que mostrara la paguina o web