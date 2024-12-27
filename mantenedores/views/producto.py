from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Producto
from ..forms import ProductoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def producto_list(request):
	productos = Producto.objects.all()
	page = Paginator(productos, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'producto/list.html', {'page': page})

def producto_detail(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	return render(request, 'producto/detail.html', {'producto': producto})

@login_required
def producto_create(request):
	if request.method == "POST":
		form = ProductoForm(request.POST)
		if form.is_valid():
			producto = form.save()
			return redirect('producto_list')
	else:
		form = ProductoForm()
	return render(request, 'producto/form.html', {'form': form})

@login_required
def producto_update(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	if request.method == "POST":
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('producto_list')
	else:
		form = ProductoForm(instance=producto)
	return render(request, 'producto/form.html', {'form': form})

@login_required
@require_POST
def producto_delete(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	producto.delete()
	return JsonResponse({'status': 'success'}, status=200)