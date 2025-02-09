from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Material
from ..forms import MaterialForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def material_list(request):
	material = Material.objects.all()
	page = Paginator(material, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'material/list.html', {'page': page})

def material_detail(request, pk):
	cargo = get_object_or_404(Material, pk=pk)
	return render(request, 'material/detail.html', {'cargo': cargo})

@login_required
def material_create(request):
	if request.method == "POST":
		form = MaterialForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('material_list')
	else:
		form = MaterialForm()
	return render(request, 'material/form.html', {'form': form})

@login_required
def material_update(request, pk):
	cargo = get_object_or_404(Material, pk=pk)
	if request.method == "POST":
		form = MaterialForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('material_list')
	else:
		form = MaterialForm(instance=cargo)
	return render(request, 'material/form.html', {'form': form})

@login_required
@require_POST
def material_delete(request, pk):
	cargo = get_object_or_404(Material, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)