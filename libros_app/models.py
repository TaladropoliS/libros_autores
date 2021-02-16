from django.db import models
# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    apellido = models.CharField(max_length=255, null=True)
    notas = models.CharField(max_length=255, null=True)
    libros = models.ManyToManyField(Libro, related_name="autores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
