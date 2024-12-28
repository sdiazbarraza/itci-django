from django import forms
from ..models import CausaRaiz

class CausaRaizForm(forms.ModelForm):

	class Meta:
		model = CausaRaiz
		fields = ['id_causa_raiz', 'nombre']

	def __init__(self, *args, **kwargs):
		super(CausaRaizForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_causa_raiz'].widget.attrs['readonly'] = True