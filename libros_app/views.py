from django.shortcuts import render, redirect
from .models import Libro, Autor
from django.contrib import messages
# Create your views here.

def inicio(request):
    if 'inicio' in request.session: # ve si ya se ha ingresó a la página.

        error = {}  # se crea vacío para poder enviar mensaje de error más abajo.
        if 'titulo' in request.POST:
            if len(request.POST['titulo']) > 0:  # verifica si 'titulo' esta vacío.
                if len(request.POST['desc']) > 0: # verifica si 'desc' esta vacío.
                    add_libro = Libro.objects.create(titulo=request.POST['titulo'], desc=request.POST['desc'])
                else:  # se comprueba el error y se entrega un mensaje.
                    error['falta_dato'] = ". . . . . < < < debe ingresar Título y Descripción > > > . . . . ."
            else:  # se comprueba el error y se entrega un mensaje.
                error['falta_dato'] = ". . . . . < < < debe ingresar Título y Descripción > > > . . . . ."
            if len(error) > 0:
                for key, msg in error.items():
                    messages.error(request, msg)

    request.session['inicio'] = True

    libros = Libro.objects.all()
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, 'index.html', context)

def autores(request):
    if 'agregar_autor' in request.session: # ve si ya se ha ingresó a la página.

        error = {}  # se crea vacío para poder enviar mensaje de error más abajo.
        if 'nombre' in request.POST:
            if len(request.POST['nombre']) > 0:  # verifica si 'nombre' esta vacío.
                if len(request.POST['apellido']) > 0:  # verifica si 'apellido' esta vacío.
                    if len(request.POST['notas']) > 0:  # verifica si 'notas' esta vacío.
                        add_autor = Autor.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], notas=request.POST['notas'])
                    else:  # se comprueba el error y se entrega un mensaje.
                        error['falta_dato'] = ". . . . . < < < debe ingresar Nombre, Apellido y Notas > > > . . . . ."
                else:  # se comprueba el error y se entrega un mensaje.
                    error['falta_dato'] = ". . . . . < < < debe ingresar Nombre, Apellido y Notas > > > . . . . ."
            else:  # se comprueba el error y se entrega un mensaje.
                error['falta_dato'] = ". . . . . < < < debe ingresar Nombre, Apellido y Notas > > > . . . . ."

            if len(error) > 0:
                for key, msg in error.items():
                    messages.error(request, msg)

    request.session['agregar_autor'] = True

    autores = Autor.objects.all()
    context = {
        "autores": Autor.objects.all()
    }
    return render(request, 'autores.html', context)

def ver_autor(request,id):
    temp = Autor.objects.get(id=id)
    context = {
        "libros": Libro.objects.all(),
        "id": temp.id,
        "nombre": temp.nombre,
        "apellido": temp.apellido,
        "notas": temp.notas
    }
    return render(request, 'ver_autor.html', context)

def ver_libro(request, id):
    temp_l = Libro.objects.get(id=id)
    context = {
        "autores": Autor.objects.all(),
        "titulo": temp_l.titulo,
        "id": temp_l.id,
        "desc": temp_l.desc,
    }
    return render(request, 'ver_libro.html', context)

def autor_del_libro(request):
    temp_a = Autor.objects.get(id=request.POST['autor_del_libro'])
    temp_l = Libro.objects.get(id=id)
    temp_l.autores.add(temp_a)
    print('id')
    return redirect('/ver_libro/{id}')