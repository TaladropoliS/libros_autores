from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('autores', views.autores),
    path('ver_autor', views.ver_autor),
    path('ver_libro', views.ver_libro),
]