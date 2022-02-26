
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) #fecha de creación
    fm = models.DateTimeField(auto_now=True)     #fecha de modificación
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #usuario de creación
    um = models.IntegerField(blank=True, null=True) #usuario de modificación

    class Meta:
        # se ignora este modelo al momento de hacer las migraciones
        abstract=True