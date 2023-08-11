from django import forms

class FormularioAgregarPrd(forms.Form):
    serialNumber=forms.CharField(label="numero de serie", required=True) 
    marca=forms.CharField(label="Marca", required=True)
    modelo=forms.CharField(label="Modelo", required=True)
    generacion=forms.IntegerField(label="Generacion", required=True)
    PArea=forms.CharField(label="PArea", required=True)## gamer, oficinista
    precio=forms.FloatField(label="Precio", required=True)
    color=forms.CharField(label="Color", required=True)
    
    #imagen=forms.ImageField(upload_to='productos/', default='default.jpg')