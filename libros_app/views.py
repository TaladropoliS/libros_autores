from django.shortcuts import render, redirect
from .models import Libro, Autor
from django.contrib import messages
# Create your views here.

def inicio(request):
    if 'inicio' in request.session: # ve si ya se ha entrado a la sesión.

        error = {}  # se crea vacío para poder enviar mensaje de error más abajo.
        if 'titulo' in request.POST:
            if len(request.POST['titulo']) > 0:  # verifica si 'titulo' esta vacío.
                # if 'titulo' in request.POST:
                # print(request.POST['titulo'])
                add_libro = Libro.objects.create(  # se crea el libro y la descripción
                    titulo=request.POST['titulo'],
                    desc=request.POST['desc'],
                )
            else:  # se comprueba el error y se entrega un mensaje.
                error['titulo'] = "* * * | | | El título no ha sido ingresado | | | * * *"
            if len(error) > 0:
                for key, msg in error.items():
                    messages.error(request, msg)
                # return redirect('/')
    request.session['inicio'] = True

    libros = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'index.html', context)

# def agregar_libro(request):
#     Libro.objects.create(titulo=request.POST['titulo'], desc=request.POST['desc'])
#     autores = Libro.objects.all()
#     context = {
#         "autores": Libro.objects.all()
#     }
#     return render(request, 'index.html', context)

def agregar_libro(request):
    Libro.objects.create(titulo=request.POST['titulo'], desc=request.POST['desc'])
    return render(redirect(''))

def autores(request):
    autores = Libro.objects.all()
    context = {
        "autores": Libro.objects.all()
    }
    return render(request, 'autores.html', context)

def ver_autor(request):
    a = Libro.objects.id(id=id)
    context = {
        "autores": a
    }
    return render(request, 'ver_autor.html', context)

def ver_libro(request,id):
    temp = Libro.objects.get(id=id)
    context = {
        "titulo": temp.titulo,
        "id": temp.id,
        "desc": temp.desc,
    }
    return render(request, 'ver_libro.html', context)
