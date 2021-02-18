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
