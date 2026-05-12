from django.shortcuts import render, redirect
from .models import MovimientoStock
from .forms import MovimientoStockForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def lista_movimientos(request):
    movimientos = MovimientoStock.objects.order_by('-fecha')

    return render(request, 'inventario/lista.html', {
        'movimientos': movimientos
    })

@login_required(login_url='login')
def crear_movimiento(request):

    if request.method == 'POST':

        form = MovimientoStockForm(request.POST)

        if form.is_valid():

            movimiento = form.save()

            producto = movimiento.producto

            if movimiento.tipo == 'ENTRADA':
                producto.stock += movimiento.cantidad

            elif movimiento.tipo == 'SALIDA':

                if producto.stock >= movimiento.cantidad:
                    producto.stock -= movimiento.cantidad

                else:
                    return render(request, 'inventario/formulario.html', {
                        'form': form,
                        'error': 'No hay suficiente stock disponible para realizar esta salida.'
                    })
            producto.save()

            return redirect('lista_movimientos')

    else:
        form = MovimientoStockForm()

    return render(request, 'inventario/formulario.html', {
        'form': form
    })

@login_required(login_url='login')
def crear_entrada(request):
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST)

        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.tipo = 'ENTRADA'
            movimiento.save()

            producto = movimiento.producto
            producto.stock += movimiento.cantidad
            producto.save()

            return redirect('lista_movimientos')
    else:
        form = MovimientoStockForm(initial={'tipo': 'ENTRADA'})

    return render(request, 'inventario/formulario.html', {
        'form': form,
        'titulo': 'Registrar entrada de stock'
    })


@login_required(login_url='login')
def crear_salida(request):
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST)

        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.tipo = 'SALIDA'

            producto = movimiento.producto

            if producto.stock >= movimiento.cantidad:
                movimiento.save()
                producto.stock -= movimiento.cantidad
                producto.save()

                return redirect('lista_movimientos')
            else:
                return render(request, 'inventario/formulario.html', {
                    'form': form,
                    'titulo': 'Registrar salida de stock',
                    'error': 'No hay suficiente stock disponible para realizar esta salida.'
                })
    else:
        form = MovimientoStockForm(initial={'tipo': 'SALIDA'})

    return render(request, 'inventario/formulario.html', {
        'form': form,
        'titulo': 'Registrar salida de stock'
    })