from django.shortcuts import render, redirect
from .models import Libro, Autor
# Create your views here.

def inicio(request):
    context = {
        "inicio": Libro.objects.all()
    }
    return render(request, 'index.html', context)
