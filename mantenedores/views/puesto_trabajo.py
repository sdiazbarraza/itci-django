from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import PuestoTrabajo
from ..forms import PuestoTrabajoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def puesto_trabajo_list(request):
	cargos = PuestoTrabajo.objects.all()
	page = Paginator(cargos, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'puesto_trabajo/list.html', {'page': page})

def puesto_trabajo_detail(request, pk):
	cargo = get_object_or_404(PuestoTrabajo, pk=pk)
	return render(request, 'puesto_trabajo/detail.html', {'cargo': cargo})

@login_required
def puesto_trabajo_create(request):
	if request.method == "POST":
		form = PuestoTrabajoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('puesto_trabajo_list')
	else:
		form = PuestoTrabajoForm()
	return render(request, 'puesto_trabajo/form.html', {'form': form})

@login_required
def puesto_trabajo_update(request, pk):
	cargo = get_object_or_404(PuestoTrabajo, pk=pk)
	if request.method == "POST":
		form = PuestoTrabajoForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('puesto_trabajo_list')
	else:
		form = PuestoTrabajoForm(instance=cargo)
	return render(request, 'puesto_trabajo/form.html', {'form': form})

@login_required
@require_POST
def puesto_trabajo_delete(request, pk):
	cargo = get_object_or_404(PuestoTrabajo, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)