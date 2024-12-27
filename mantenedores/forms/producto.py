from django import forms
from ..models import Producto

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ['id_producto', 'nombre']

	def __init__(self, *args, **kwargs):
		super(ProductoForm, self).__init__(*args, **kwargs)
		if self.instance and self.instance.pk:
			self.fields['id_producto'].widget.attrs['readonly'] = True