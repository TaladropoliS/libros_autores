from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('agregar_libro', views.inicio),
    path('agregar_autor', views.autores),
    path('ver_autor', views.ver_autor),
    path('ver_autor/<int:id>', views.ver_autor),
    path('ver_libro', views.ver_libro),
    path('ver_libro/<int:id>', views.ver_libro),
]