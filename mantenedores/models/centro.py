from django.db import models

# Create your models here.
class Centro(models.Model):

    id = models.AutoField(primary_key=True)
    id_centro = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tbl_centro'