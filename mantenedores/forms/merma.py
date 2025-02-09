from django import forms
from ..models import Merma, TipoMerma

class MermaForm(forms.ModelForm):
    tipo_merma = forms.ModelChoiceField(queryset=TipoMerma.objects.all(), widget=forms.Select)

    class Meta:
        model = Merma
        fields = ['nombre', 'tipo_merma']
