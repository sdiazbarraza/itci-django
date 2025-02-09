from django.db import models

class Material(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    formato = models.CharField(max_length=255)
    peso_caja = models.CharField(max_length=255)
    golpes = models.CharField(max_length=255)
    bajadas = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tbl_material'