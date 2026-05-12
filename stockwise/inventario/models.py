from django.db import models
from productos.models import Producto

class MovimientoStock(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre}"