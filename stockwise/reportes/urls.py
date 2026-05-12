from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes, name='reportes'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
    path(
    'exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
]