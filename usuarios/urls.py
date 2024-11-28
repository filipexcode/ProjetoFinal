from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
]