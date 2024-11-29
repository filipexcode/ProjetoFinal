from django import forms
from .models import Consulta
from procedimentos.models import Procedimento

class ConsultaForm(forms.ModelForm):
    procedimento = forms.ModelChoiceField(
        queryset=Procedimento.objects.all(),
        widget=forms.Select,
        empty_label="Selecione um procedimento"
    )  # Campo com lista suspensa

    class Meta:
        model = Consulta
        fields = ['paciente', 'data_hora', 'procedimento']  # Inclua o campo procedimento
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
