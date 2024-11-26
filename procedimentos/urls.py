from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_procedimentos, name='lista_procedimentos'),
    path('novo/', views.cria_procedimento, name='cria_procedimento'),
    path('editar/<int:pk>/', views.edita_procedimento, name='edita_procedimento'),
    path('excluir/<int:pk>/', views.exclui_procedimento, name='exclui_procedimento'),
]
