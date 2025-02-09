from django import forms
from ..models import Material

class MaterialForm(forms.ModelForm):

	class Meta:
		model = Material		    
		fields = ['nombre', 'formato', 'peso_caja', 'golpes', 'bajadas']

