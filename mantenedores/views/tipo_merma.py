from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import TipoMerma
from ..forms import TipoMermaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def tipo_merma_list(request):
	tipo_merma = TipoMerma.objects.all()
	page = Paginator(tipo_merma, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'tipo_merma/list.html', {'page': page})

def tipo_merma_detail(request, pk):
	cargo = get_object_or_404(TipoMerma, pk=pk)
	return render(request, 'tipo_merma/detail.html', {'cargo': cargo})

@login_required
def tipo_merma_create(request):
	if request.method == "POST":
		form = TipoMermaForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('tipo_merma_list')
	else:
		form = TipoMermaForm()
	return render(request, 'tipo_merma/form.html', {'form': form})

@login_required
def tipo_merma_update(request, pk):
	cargo = get_object_or_404(TipoMerma, pk=pk)
	if request.method == "POST":
		form = TipoMermaForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('tipo_merma_list')
	else:
		form = TipoMermaForm(instance=cargo)
	return render(request, 'tipo_merma/form.html', {'form': form})

@login_required
@require_POST
def tipo_merma_delete(request, pk):
	cargo = get_object_or_404(TipoMerma, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)