from django import forms
from ..models import Turno

class TurnoForm(forms.ModelForm):

    class Meta:
        model = Turno
        fields = ['nombre', 'hora_inicio', 'hora_fin']
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }