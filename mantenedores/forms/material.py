from django import forms
from ..models import Material

class MaterialForm(forms.ModelForm):

	class Meta:
		model = Material		    
		fields = ['nombre', 'formato', 'peso_caja', 'golpes', 'bajadas', 'unidad_caja']
		labels = {
				'unidad_caja': 'Unidad por Caja',
				'peso_caja': 'Peso por Caja'  # Cambia el label de 'unidad_caja'
			}
