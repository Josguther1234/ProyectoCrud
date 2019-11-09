from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^empleado/', views.ListaEmpleado, name='ListaEmpleado'),
    url(r'^empleado/nuevo/$', views.NuevoEmpleado, name='NuevoEmpleado'),

    url(r'^animal/', views.ListaAnimal, name='ListaAnimal'),

    url(r'^hc/', views.ListaHorairoCuidado, name='ListaHorarioCuidado'),
]
