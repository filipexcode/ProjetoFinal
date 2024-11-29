from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta
from .forms import ConsultaForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/lista.html', {'consultas': consultas})

def cria_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')  # Redirecione após salvar
    else:
        form = ConsultaForm()

    return render(request, 'consultas/formulario.html', {'form': form})

def edita_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consultas/formulario.html', {'form': form})

def exclui_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('lista_consultas')
    return render(request, 'consultas/confirma_exclusao.html', {'consulta': consulta})
