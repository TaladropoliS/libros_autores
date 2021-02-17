from django.shortcuts import render, redirect
from .models import Libro, Autor
from django.contrib import messages
# Create your views here.

def inicio(request):
    if 'inicio' in request.session:

        error = {}
        if len(request.POST['titulo'])>0:
        # if 'titulo' in request.POST:
            print(request.POST['titulo'])
            libro_add = Libro.objects.create(
                titulo=request.POST['titulo'],
                desc=request.POST['desc']
            )
        else:
            error['titulo']="No ingresó datos"

        if len(error) > 0:
            for key, msg in error.items():
                messages.error(request, msg)
            # return redirect('/')
    request.session['inicio'] = True
    libro_todos = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }

    return render(request, 'index.html', context)
