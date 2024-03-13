from django.shortcuts import render
from .models import Vuelo

# Create your views here.
def home(request):
	return render(request, 'home.html')

def listar(request):
	vuelos = Vuelo.objects.all()
	return render(request, 'listar.html', {'vuelos': vuelos})

def registrar(request):
	return render(request, 'home.html')

def estadisticas(request):
	return render(request, 'home.html')