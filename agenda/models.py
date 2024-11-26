from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.data} às {self.horario}"
