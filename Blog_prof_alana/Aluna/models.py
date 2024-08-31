from django.db import models

# Create your models here.
class Aluno(models.Model):
    data = models.DateField()
    titulo = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.descricao
    

class Sobre(models.Model):
    data_nascimento = models.DateField()
    titulo = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.descricao
    
    
class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    

class Convidados(models.Model):
    nome = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    

class Casamento(models.Model):
    descricao = models.TextField()
    data = models.CharField(max_length=100)
    hora = models.TimeField()
    local = models.CharField(max_length=100)
    convidados = models.ForeignKey(Convidados, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.descricao