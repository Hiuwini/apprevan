from django.db import models
from django.utils import timezone

# Create your models here.
class Participante(models.Model):
    p_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre + self.apellido

class Evento(models.Model):
    e_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Beneficio(models.Model):
    p_id = models.ForeignKey('Participante', on_delete=models.CASCADE)
    e_id = models.ForeignKey('Evento', on_delete=models.CASCADE)
