from django.urls import path
from . import views

urlpatterns = [
    path('calendario/', views.calendario, name='calendario'),
    path('eventos/', views.eventos, name='get_eventos'),  # Alterado para apontar para a função correta
]
