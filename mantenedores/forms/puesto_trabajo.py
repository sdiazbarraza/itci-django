from django import forms
from ..models import PuestoTrabajo

class PuestoTrabajoForm(forms.ModelForm):

	class Meta:
		model = PuestoTrabajo
		fields = ['id_puesto_trabajo', 'nombre']

	def __init__(self, *args, **kwargs):
		super(PuestoTrabajoForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_puesto_trabajo'].widget.attrs['readonly'] = True