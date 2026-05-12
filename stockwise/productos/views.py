from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CategoriaForm

@login_required(login_url='login')
def lista_productos(request):
    query = request.GET.get('buscar')

    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()

    return render(request, 'productos/lista.html', {
        'productos': productos,
        'query': query
    })

@login_required(login_url='login')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/formulario.html', {'form': form})

@login_required(login_url='login')
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/formulario.html', {'form': form})

@login_required(login_url='login')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')

@login_required(login_url='login')
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/categorias.html', {
        'categorias': categorias
    })


@login_required(login_url='login')
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'productos/formulario_categoria.html', {
        'form': form
    })


@login_required(login_url='login')
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'productos/formulario_categoria.html', {
        'form': form
    })


@login_required(login_url='login')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('lista_categorias')