from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import UnidadMedida
from ..forms import UnidadMedidaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def unidad_medida_list(request):
	unidad_medida = UnidadMedida.objects.all()
	page = Paginator(unidad_medida, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'unidad_medida/list.html', {'page': page})

def unidad_medida_detail(request, pk):
	_instance = get_object_or_404(UnidadMedida, pk=pk)
	return render(request, 'unidad_medida/detail.html', {'_instance': _instance})

@login_required
def unidad_medida_create(request):
	if request.method == "POST":
		form = UnidadMedidaForm(request.POST)
		if form.is_valid():
			_instance = form.save()
			return redirect('unidad_medida_list')
	else:
		form = UnidadMedidaForm()
	return render(request, 'unidad_medida/form.html', {'form': form})

@login_required
def unidad_medida_update(request, pk):
	_instance = get_object_or_404(UnidadMedida, pk=pk)
	if request.method == "POST":
		form = UnidadMedidaForm(request.POST, instance=_instance)
		if form.is_valid():
			form.save()
			return redirect('unidad_medida_list')
	else:
		form = UnidadMedidaForm(instance=_instance)
	return render(request, 'unidad_medida/form.html', {'form': form})

@login_required
@require_POST
def unidad_medida_delete(request, pk):
	_instance = get_object_or_404(UnidadMedida, pk=pk)
	_instance.delete()
	return JsonResponse({'status': 'success'}, status=200)