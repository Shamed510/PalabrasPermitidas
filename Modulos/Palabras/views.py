from django.shortcuts import render, redirect
from .models import Palabras
from datetime import datetime

# Create your views here.

def home(request):
    palabrasList = Palabras.objects.all()
    return render(request, "index.html", {"Palabras" : palabrasList})

def agregarPalabra(request):
    #obtenemos los datos enviados del metodo POST en HTML y los guardamos en
    #variables para redirigir dichos datos a la bd de 'models.py'
    palabra = request.POST['Palabra']
    allow = request.POST['btnradio']
    #Creamos la palabra nueva asignando a los nombres de los campos en /models.py
    #cada variable creada arriba donde obtenemos los datos ingresado del metodo POST
    #enviados desde HTML en el formulario
    nueva = Palabras.objects.create(
    word = palabra,
    allowed = allow)

    #Regresamos al usuario a la ruita raiz
    return redirect('/')

def editarPalabra(request, id):
    palabra = Palabras.objects.get(id = id)
    return render(request, "edicionPalabra.html", {"palabra":palabra})

def edicionPalabra(request):
    #Obtenemos los elementos necesarios de POST en el html editarPalabra
    id = request.POST['txtId']
    palabra = request.POST['Palabra']
    allow = request.POST['btnradio']

    #Asignamos dichos elementos a la misma palabra para editarlo y guardamos
    uPalabra = Palabras.objects.get(id = id)
    uPalabra.word = palabra
    uPalabra.allowed = allow
    uPalabra.lastUpdate = datetime.today().strftime('%Y-%m-%d %H:%M')
    uPalabra.save()

    return redirect('/')

def borrarPalabra(request, id):
     #Obtenemos los elementos necesarios de POST en el html editarPalabra
    uPalabra = Palabras.objects.get(id = id)

    #Asignamos dichos elementos a la misma palabra para editarlo y guardamos
    uPalabra = Palabras.objects.get(id = id)
    uPalabra.word += ' DELETED'
    uPalabra.allowed = False
    uPalabra.status = 'Deleted'
    uPalabra.dateDeleted = datetime.today().strftime('%Y-%m-%d %H:%M')
    uPalabra.save()

    return redirect('/')