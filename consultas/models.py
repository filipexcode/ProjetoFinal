from django.utils import timezone
from django.db import models

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    dentista = models.CharField(max_length=100)
    data_hora = models.DateTimeField(default=timezone.now)
    procedimento = models.CharField(max_length=200, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.paciente} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
