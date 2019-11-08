from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def ListaEmpleado(request):
    return render(request,'empleado/ListaEmpleado.html')
