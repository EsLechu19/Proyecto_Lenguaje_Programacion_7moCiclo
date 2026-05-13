from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productos.models import Producto, Categoria
from inventario.models import MovimientoStock


@login_required(login_url='login')
def dashboard(request):
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    total_entradas = MovimientoStock.objects.filter(tipo='ENTRADA').count()
    total_salidas = MovimientoStock.objects.filter(tipo='SALIDA').count()

    productos_stock_bajo = Producto.objects.filter(stock__lte=5)
    ultimos_movimientos = MovimientoStock.objects.order_by('-fecha')[:5]

    nombres_productos = []
    stock_actual = []
    stock_minimo = []

    productos = Producto.objects.order_by('stock')[:5]

    for producto in productos:
        nombres_productos.append(producto.nombre)
        stock_actual.append(producto.stock)
        stock_minimo.append(producto.stock_minimo)

    context = {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_entradas': total_entradas,
        'total_salidas': total_salidas,
        'productos_stock_bajo': productos_stock_bajo,
        'ultimos_movimientos': ultimos_movimientos,
        'nombres_productos': nombres_productos,
        'stock_actual': stock_actual,
        'stock_minimo': stock_minimo,
    }

    return render(request, 'dashboard.html', context)