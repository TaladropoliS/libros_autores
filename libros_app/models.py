from django.db import models
# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # autores --- hace la relación con libros ---

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    apellido = models.CharField(max_length=255, null=True)
    notas = models.CharField(max_length=255, null=True)
    libros = models.ManyToManyField(Libro, related_name="autores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # libros --- hace la relación con autores ---

    def __str__(self):
        return self.nombre + " " + self.apellido