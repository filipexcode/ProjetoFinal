from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_consultas, name='lista_consultas'),
    path('novo/', views.cria_consulta, name='cria_consulta'),
    path('editar/<int:pk>/', views.edita_consulta, name='edita_consulta'),
    path('excluir/<int:pk>/', views.exclui_consulta, name='exclui_consulta'),
]
