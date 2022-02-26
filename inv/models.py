
from tabnanny import verbose
from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoria',
        unique=True
    )

    def __str__(self):
        """ Descripción del modelo categoria"""
        return '{}'.format(self.descripcion)

    def save(self):
        """ el valor de categoría lo guardamos en mayusculas"""
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"