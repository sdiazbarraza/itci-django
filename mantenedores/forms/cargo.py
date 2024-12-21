from django import forms
from ..models import Cargo

class CargoForm(forms.ModelForm):
	class Meta:
		model = Cargo
		fields = ['id_cargo', 'nombre']