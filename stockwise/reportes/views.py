from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from productos.models import Producto, Categoria
from inventario.models import MovimientoStock


@login_required(login_url='login')
def reportes(request):

    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()

    total_entradas = MovimientoStock.objects.filter(
        tipo='ENTRADA'
    ).count()

    total_salidas = MovimientoStock.objects.filter(
        tipo='SALIDA'
    ).count()

    productos_stock_bajo = Producto.objects.filter(
        stock__lte=5
    )

    ultimos_movimientos = MovimientoStock.objects.order_by(
        '-fecha'
    )[:10]

    return render(request, 'reportes/reportes.html', {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_entradas': total_entradas,
        'total_salidas': total_salidas,
        'productos_stock_bajo': productos_stock_bajo,
        'ultimos_movimientos': ultimos_movimientos,
    })