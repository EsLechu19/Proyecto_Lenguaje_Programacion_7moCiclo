from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_movimientos, name='lista_movimientos'),
    path('crear/', views.crear_movimiento, name='crear_movimiento'),
    path('entrada/', views.crear_entrada, name='crear_entrada'),
    path('salida/', views.crear_salida, name='crear_salida'),
]