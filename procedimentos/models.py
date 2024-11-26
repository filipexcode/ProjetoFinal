from django.db import models

class Procedimento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.IntegerField(help_text="Duração em minutos")

    def __str__(self):
        return self.nome
