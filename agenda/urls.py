from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('eventos/', views.get_eventos, name='get_eventos'),
]
