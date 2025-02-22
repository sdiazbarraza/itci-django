from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Cargo
from ..forms import CargoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def cargo_list(request):
	cargos = Cargo.objects.all()
	page = Paginator(cargos, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'cargo/list.html', {'page': page})

def cargo_detail(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	return render(request, 'cargo/detail.html', {'cargo': cargo})

@login_required
def cargo_create(request):
	if request.method == "POST":
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('cargo_list')
	else:
		form = CargoForm()
	return render(request, 'cargo/form.html', {'form': form})

@login_required
def cargo_update(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	if request.method == "POST":
		form = CargoForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('cargo_list')
	else:
		form = CargoForm(instance=cargo)
	return render(request, 'cargo/form.html', {'form': form})

@login_required
@require_POST
def cargo_delete(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)