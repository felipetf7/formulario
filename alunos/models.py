from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    email = models.EmailField()
    endereco = models.TextField()
    def __str__(self):
        return self.nome

