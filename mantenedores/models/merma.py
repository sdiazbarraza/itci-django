from django.db import models
from ..models import TipoMerma

class Merma(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo_merma = models.ForeignKey(TipoMerma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tbl_merma'