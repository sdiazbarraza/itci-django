from django.db import models

class Producto(models.Model):

    id = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tbl_producto'