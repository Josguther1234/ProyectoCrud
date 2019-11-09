from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^empleado/', views.ListaEmpleado, name='ListaEmpleado'),
    url(r'^nuevoE/', views.NuevoEmpleado, name='NuevoEmpleado'),
    #url(r'^empleado/(?P<pk>[0-9]+)/eliminar/$', views.EliminarEmpleado, name='EliminarEmpleado'),
    path('empleado/<int:pk>/', views.EliminarEmpleado, name='EliminarEmpleado'),

    url(r'^animal/', views.ListaAnimal, name='ListaAnimal'),
    url(r'^nuevoA/', views.NuevoAnimal, name='NuevoAnimal'),

    url(r'^hc/', views.ListaHorairoCuidado, name='ListaHorarioCuidado'),
]
