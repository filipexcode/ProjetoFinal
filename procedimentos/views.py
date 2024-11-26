from django.shortcuts import render, get_object_or_404, redirect
from .models import Procedimento
from .forms import ProcedimentoForm
from django.http import HttpResponse

def lista_procedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimentos/lista.html', {'procedimentos': procedimentos})

def cria_procedimento(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_procedimentos')
    else:
        form = ProcedimentoForm()
    return render(request, 'procedimentos/formulario.html', {'form': form})

def edita_procedimento(request, pk):
    procedimento = get_object_or_404(Procedimento, pk=pk)
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, instance=procedimento)
        if form.is_valid():
            form.save()
            return redirect('lista_procedimentos')
    else:
        form = ProcedimentoForm(instance=procedimento)
    return render(request, 'procedimentos/formulario.html', {'form': form})

def exclui_procedimento(request, pk):
    procedimento = get_object_or_404(Procedimento, pk=pk)
    if request.method == 'POST':
        procedimento.delete()
        return redirect('lista_procedimentos')
    return render(request, 'procedimentos/confirma_exclusao.html', {'procedimento': procedimento})
