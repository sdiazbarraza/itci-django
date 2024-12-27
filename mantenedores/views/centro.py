from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Centro
from ..forms import CentroForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def centro_list(request):
	centros = Centro.objects.all()
	page = Paginator(centros, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'centro/list.html', {'page': page})

def centro_detail(request, pk):
	centro = get_object_or_404(Centro, pk=pk)
	return render(request, 'centro/detail.html', {'centro': centro})

@login_required
def centro_create(request):
	if request.method == "POST":
		form = CentroForm(request.POST)
		if form.is_valid():
			centro = form.save()
			return redirect('centro_list')
	else:
		form = CentroForm()
	return render(request, 'centro/form.html', {'form': form})

@login_required
def centro_update(request, pk):
	centro = get_object_or_404(Centro, pk=pk)
	if request.method == "POST":
		form = CentroForm(request.POST, instance=centro)
		if form.is_valid():
			form.save()
			return redirect('centro_list')
	else:
		form = CentroForm(instance=centro)
	return render(request, 'centro/form.html', {'form': form})

@login_required
@require_POST
def centro_delete(request, pk):
	centro = get_object_or_404(Centro, pk=pk)
	centro.delete()
	return JsonResponse({'status': 'success'}, status=200)