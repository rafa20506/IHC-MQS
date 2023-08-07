from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    documento = open("../venta_Laptops/venta_Laptops/vistas/index.html")   # la direccion relativa de los archivos html, css "vistas"
    
    plt = Template(documento.read())  #copiar siempre
    documento.close()               #copiar siempre

    ctx = Context()                 #copiar siempre
    documentoMostrar = plt.render(ctx) #copiar siempre

    return HttpResponse(documentoMostrar)  # el elemento que mostrara la paguina o web


def despedida(request, nombre):   # lo mismo de arriba pero con parametros
    documento = open("../venta_Laptops/venta_Laptops/vistas/index.html")   # la direccion relativa de los archivos html, css "vistas"
    
    plt = Template(documento.read())  #copiar siempre
    documento.close()               #copiar siempre

    ctx = Context()                 #copiar siempre
    documentoMostrar = plt.render(ctx)%(nombre) #   %("joaquin perrra")  #copiar siempre y aqui agregar las variables todo esto

    return HttpResponse(documentoMostrar)  # el elemento que mostrara la paguina o web