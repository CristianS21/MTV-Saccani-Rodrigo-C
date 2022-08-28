
from django.db import models

class Familiar (models.Model):
    vinculo= models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_de_nacimiento= models.DateField()
    n_celular=models.IntegerField()
    


