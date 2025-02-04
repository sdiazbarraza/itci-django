from django.db import models

class Turno(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tbl_turno'