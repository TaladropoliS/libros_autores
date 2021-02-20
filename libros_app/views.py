from django.shortcuts import render, redirect
from .models import Libro, Autor
from django.contrib import messages
# Create your views here.

def inicio(request):
    libros = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'index.html', context)

def autores(request):
    autores = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'autores.html', context)

def ver_autor(request):
    autores = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'ver_autor.html', context)

def ver_libro(request):
    autores = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'ver_libro.html', context)
