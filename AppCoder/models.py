import email
from django.db import models


# Create your models here.
class family(models.Model):

    nombre = models.CharField(max_length=40)
    integrante = models.CharField(max_length=40)
    email = models.EmailField()
    nacimiento = models.DateField()
    
