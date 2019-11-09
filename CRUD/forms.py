from django.contrib.admin import widgets
from django import forms
from .models import Encargado,Animal,HorarioCuidado


class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ('nombre', 'apellido',)
