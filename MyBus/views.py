from django.shortcuts import render
from django.http import HttpResponse
from MyBus.models import Colectivo, Recorrido, Tarifa
from django.core import serializers
from MyBus.forms import *

# Create your views here.
def Principal(request):
    return render(request, 'MyBus/principal.html')

def busqueda(request):
    return render(request, 'MyBus/busquedacolectivo.html')

def buscar(request):
    codigo = request.GET['linea_colectivo']
    lineas_todas = Colectivo.objects.filter(linea_colectivo=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'MyBus/resultadocolectivo.html', {"colectivo":codigo, "colectivos_todos":lineas_todas})

def busquedarecorrido(request):
    return render(request, 'MyBus/busquedarecorrido.html')

def buscarrecorrido(request):
    codigo = request.GET['recorrido']
    recorridos_todas = Recorrido.objects.filter(linea_colectivo=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'MyBus/resultadorecorrido.html', {"recorrido":codigo, "recorridos_todos":recorridos_todas})

def busquedatarifa(request):
    return render(request, 'MyBus/busquedatarifa.html')

def buscartarifa(request):
    codigo = request.GET['tarifa']
    tarifas_todas = Tarifa.objects.filter(linea_colectivo=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'MyBus/resultadotarifa.html', {"tarifa":codigo, "tarifas_todos":tarifas_todas})

def colectivoApi(request):
    colectivo_todos = Colectivo.objects.all()
    return HttpResponse(serializers.serialize('json',colectivo_todos))

def recorridoApi(request):
    recorrido_todas = Recorrido.objects.all()
    return HttpResponse(serializers.serialize('json',recorrido_todas))

def tarifaApi(request):
    tarifa_todas = Tarifa.objects.all()
    return HttpResponse(serializers.serialize('json',tarifa_todas))

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

def colectivos(request):
    return render (request, "MyBus/iniciocolectivo.html", {})

class Colectivolist(ListView):
    model= Colectivo
    template = "Mybus/colectivo_list.html"

class Colectivocreat(CreateView):
    model= Colectivo
    fields = "__all__"
    success_url = "/MyBus/colectivo/"

class Colectivoedit(UpdateView):
    model= Colectivo
    fields = "__all__"
    success_url = "/MyBus/colectivolist/"

class Colectivodetail(DetailView):
    model= Colectivo
    fields = "__all__"
    template = "Mybus/colectivo_detail.html"

class Colectivodelete(DeleteView):
    model = Colectivo
    fields="__all__"
    success_url = "/MyBus/colectivo/"

def recorridos(request):
    return render (request, "MyBus/iniciorecorrido.html", {})

class Recorridolist(ListView):
    model= Recorrido
    template = "Mybus/recorrido_list.html"

class Recorridoscreat(CreateView):
    model= Recorrido
    fields = "__all__"
    success_url = "/MyBus/recorrido/"

class Recorridoedit(UpdateView):
    model= Recorrido
    fields = "__all__"
    success_url = "/MyBus/recorridolist/"

class Recorridodetail(DetailView):
    model= Recorrido
    fields = "__all__"
    template = "Mybus/recorrido_detail.html"

class Recorridodelete(DeleteView):
    model = Recorrido
    fields="__all__"
    success_url = "/MyBus/recorrido/"

def tarifas(request):
    return render (request, "MyBus/iniciotarifa.html", {})

class Tarifaslist(ListView):
    model= Tarifa
    template = "Mybus/tarifa_list.html"

class Tarifascreat(CreateView):
    model= Tarifa
    fields = "__all__"
    success_url = "/MyBus/tarifas/"

class Tarifasedit(UpdateView):
    model= Tarifa
    fields = "__all__"
    success_url = "/MyBus/tarifaslist/"

class Tarifasdetail(DetailView):
    model= Tarifa
    fields = "__all__"
    template = "Mybus/tarifa_detail.html"

class Tarifasdelete(DeleteView):
    model = Tarifa
    fields="__all__"
    success_url = "/MyBus/tarifas/"