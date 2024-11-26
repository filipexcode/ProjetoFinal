from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento

def calendario(request):
    return render(request, 'agenda/calendario.html')

def get_eventos(request):
    eventos = Evento.objects.all()
    eventos_json = [
        {
            "title": evento.titulo,
            "start": f"{evento.data}T{evento.horario}",
            "description": evento.descricao,
        }
        for evento in eventos
    ]
    return JsonResponse(eventos_json, safe=False)
