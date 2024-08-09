from django.db import models

# Create your models here.

class Curso (models.Model):
    nome= models.CharField(max_length=120)
    idade= models.IntegerField()
    matricula= models.IntegerField()
    
    def __str__(self):
        return self.nome