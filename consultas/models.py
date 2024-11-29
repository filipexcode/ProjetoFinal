from django.db import models
from procedimentos.models import Procedimento  # Importe o modelo de Procedimento

class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    procedimento = models.ForeignKey(
        Procedimento, 
        on_delete=models.CASCADE, 
        related_name='consultas'
    )  # Relacionamento com o modelo Procedimento

    def __str__(self):
        return f"{self.paciente} - {self.data_hora}"
