from django.shortcuts import render,get_object_or_404,redirect
from CRUD.models import Animal,Encargado,HorarioCuidado
from django.contrib import messages
from .forms import EncargadoForm,AnimalForm


def index(request):
    return render(request,'index.html')


def ListaEmpleado(request):
    encargado = Encargado.objects.all
    return render(request,'empleado/list_empleado.html',{'encargado':encargado})

def NuevoEmpleado(request):
    if request.method == "POST":
        formulario = EncargadoForm(request.POST)
        if formulario.is_valid():
            encargado = Encargado(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'])
            encargado.save()
            messages.add_message(request,messages.SUCCESS,'Datos Guardados')
        return redirect('ListaEmpleado')
    else:
        formulario = EncargadoForm()
    return render(request,'empleado/EditarEmpleado.html')

def EliminarEmpleado(request, pk):
    encargado = Encargado.objects.get(pk=pk)
    #encargado = get_object_or_404(Encargado, id=pk)
    encargado.delete()
    return redirect('ListaEmpleado')


def ListaAnimal(request):
    animal = Animal.objects.all
    return render(request,'animal/list_animal.html',{'animal':animal})

def NuevoAnimal(request):
    if request.method == "POST":
        formulario = AnimalForm(request.POST)
        if formulario.is_valid():
            animal = Animal(nombre=formulario.cleaned_data['nombre'],
            tipo=formulario.cleaned_data['tipo'],
            edad=formulario.cleaned_data['edad'],
            cantidad=formulario.cleaned_data['cantidad'])
            animal.save()
            messages.add_message(request,messages.SUCCESS,'Datos Guardados')
        return redirect('ListaAnimal')
    else:
        formulario = AnimalForm()
    return render(request,'animal/EditarAnimal.html')


def ListaHorairoCuidado(request):
    horariocuidado = HorarioCuidado.objects.all
    return render(request,'HorarioCuidado/list_hc.html',{'horariocuidado':horariocuidado})
