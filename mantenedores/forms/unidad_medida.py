from django import forms
from ..models import UnidadMedida

class UnidadMedidaForm(forms.ModelForm):

	class Meta:
		model = UnidadMedida
		fields = ['id_unidad_medida', 'nombre']

	def __init__(self, *args, **kwargs):
		super(UnidadMedidaForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_unidad_medida'].widget.attrs['readonly'] = True