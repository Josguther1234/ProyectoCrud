from django.db import models
from django.contrib import admin

class Animal(models.Model):
    nombre = models.CharField(max_length=70)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Encargado(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

class HorarioCuidado(models.Model):
    fecha_cuidado = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    def __str__(self):
        return self.encargado.str()

class HorarioCuidadoInLine(admin.TabularInline):
    model = HorarioCuidado
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    inlines = (HorarioCuidadoInLine,)

class EncargadoAdmin (admin.ModelAdmin):
    inlines = (HorarioCuidadoInLine,)
