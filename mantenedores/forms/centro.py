from django import forms
from ..models import Centro

class CentroForm(forms.ModelForm):

	class Meta:
		model = Centro
		fields = ['id_centro', 'nombre']

	def __init__(self, *args, **kwargs):
		super(CentroForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_centro'].widget.attrs['readonly'] = True