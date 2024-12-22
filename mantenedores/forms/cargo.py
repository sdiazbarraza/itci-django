from django import forms
from ..models import Cargo

class CargoForm(forms.ModelForm):

	class Meta:
		model = Cargo
		fields = ['id_cargo', 'nombre']

	def __init__(self, *args, **kwargs):
		super(CargoForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_cargo'].widget.attrs['readonly'] = True