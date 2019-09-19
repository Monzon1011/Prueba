from django.shortcuts import render, render_to_response

from models import Persona
from models import Producto
from models import Compra

# Create your views here.

def listarProductos(request):
    p = Producto.objects.all()
    return render_to_response('Producto.html', { 'productos' : p })

def listarPersonas(request):
    per = Persona.objects.all()
    return render_to_response('Personas.html', { 'personas' : per })

def listarCompra(request):
    if request.GET.get('id'):
        idCompra = request.GET.get('id')
        c = Compra.objects.filter(id=idCompra)
    else:
        c = Compra.objects.all()
        return render_to_response('Compra.html', { 'compras' : c })
