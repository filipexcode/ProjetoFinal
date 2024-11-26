from django.test import TestCase
from django.urls import reverse
from .models import Procedimento

class ProcedimentoModelTest(TestCase):
    
    def setUp(self):
        self.procedimento = Procedimento.objects.create(nome='Limpeza Dental', descricao='Limpeza completa dos dentes')

    def test_procedimento_creation(self):
        """Teste se o procedimento foi criado corretamente"""
        procedimento = Procedimento.objects.get(nome='Limpeza Dental')
        self.assertEqual(procedimento.nome, 'Limpeza Dental')
        self.assertEqual(procedimento.descricao, 'Limpeza completa dos dentes')

    def test_procedimento_update(self):
        """Teste se o procedimento foi atualizado corretamente"""
        self.procedimento.nome = 'Limpeza Profunda'
        self.procedimento.save()
        procedimento = Procedimento.objects.get(id=self.procedimento.id)
        self.assertEqual(procedimento.nome, 'Limpeza Profunda')

    def test_procedimento_deletion(self):
        """Teste se o procedimento foi excluído corretamente"""
        procedimento_id = self.procedimento.id
        self.procedimento.delete()
        with self.assertRaises(Procedimento.DoesNotExist):
            Procedimento.objects.get(id=procedimento_id)

    def test_procedimento_list_view(self):
        """Teste a view de listagem de procedimentos"""
        response = self.client.get(reverse('procedimentos:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Limpeza Dental')

    def test_procedimento_create_view(self):
        """Teste a view de criação de procedimento"""
        data = {'nome': 'Extração Dental', 'descricao': 'Remoção de dente'}
        response = self.client.post(reverse('procedimentos:create'), data)
        self.assertEqual(response.status_code, 302)  
        procedimento = Procedimento.objects.get(nome='Extração Dental')
        self.assertEqual(procedimento.descricao, 'Remoção de dente')

    def test_procedimento_update_view(self):
        """Teste a view de edição de procedimento"""
        data = {'nome': 'Limpeza Dental', 'descricao': 'Limpeza de dentes e gengivas'}
        response = self.client.post(reverse('procedimentos:update', args=[self.procedimento.id]), data)
        self.assertEqual(response.status_code, 302)  
        procedimento = Procedimento.objects.get(id=self.procedimento.id)
        self.assertEqual(procedimento.descricao, 'Limpeza de dentes e gengivas')
