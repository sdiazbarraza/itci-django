from django import forms
from ..models import TipoMerma

class TipoMermaForm(forms.ModelForm):

	class Meta:
		model = TipoMerma
		fields = ['id_tipo_merma', 'nombre']

	def __init__(self, *args, **kwargs):
		super(TipoMermaForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_tipo_merma'].widget.attrs['readonly'] = True