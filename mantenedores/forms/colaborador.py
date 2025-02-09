from django import forms
from ..models import Colaborador, Cargo

class ColaboradorForm(forms.ModelForm):
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), widget=forms.Select)

    class Meta:
        model = Colaborador
        fields = ['nombre', 'rut', 'apellido', 'telefono', 'correo', 'cargo']
