from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento
from consultas.models import Consulta
from datetime import timedelta
from django.contrib.auth.decorators import login_required

@login_required
def calendario(request):
    return render(request, 'agenda/calendario.html')

from datetime import timedelta

def eventos(request):
    consultas = Consulta.objects.select_related('procedimento').all()
    eventos = []

    for consulta in consultas:
        duracao_em_horas = consulta.procedimento.duracao
        hora_inicio = consulta.data_hora
        hora_fim = hora_inicio + timedelta(hours=duracao_em_horas)

        # Ajustar o horário final para não ultrapassar o mesmo dia
        if hora_fim.date() != hora_inicio.date():
            hora_fim = hora_inicio.replace(hour=23, minute=59, second=59)

        eventos.append({
            'title': f"{consulta.paciente} - {consulta.procedimento.nome}",  # Apenas paciente e procedimento
            'start': hora_inicio.isoformat(),
            'end': hora_fim.isoformat(),
            'backgroundColor': '#f39c12',
            'borderColor': '#e67e22',
            'textColor': '#ffffff',  # Cor do texto para contraste
        })

    return JsonResponse(eventos, safe=False)



