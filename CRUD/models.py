from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=70)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    cantidad = models.IntegerField()
