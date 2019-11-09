from django.shortcuts import render,get_object_or_404,redirect
from CRUD.models import Animal,Encargado,HorarioCuidado
from django.contrib import messages
from .forms import EncargadoForm

def index(request):
    return render(request,'index.html')


def ListaEmpleado(request):
    encargado = Encargado.objects.all
    return render(request,'empleado/list_empleado.html',{'encargado':encargado})

def NuevoEmpleado(request):
    if request.method == "POST":
        formulario = EncargadoForm(request.POST)
        if formulario.is_valid():
            encargado = formulario.save(commit=false)
            encargado = Encargado(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'])
            encargado.save()
            messages.add_message(request,messages.SUCCESS,'Datos Guardados')
        return redirect('index')
    else:
        formulario = EncargadoForm()
    return render(request,'index.html')

def ListaAnimal(request):
    animal = Animal.objects.all
    return render(request,'animal/list_animal.html',{'animal':animal})


def ListaHorairoCuidado(request):
    horariocuidado = HorarioCuidado.objects.all
    return render(request,'HorarioCuidado/list_hc.html',{'horariocuidado':horariocuidado})
