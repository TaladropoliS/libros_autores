from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('agregar_libro', views.agregar_libro),
    path('autores', views.autores),
    path('ver_autor', views.ver_autor),
    path('ver_libro', views.ver_libro),
    path('ver_libro/<int:id>', views.ver_libro),
]