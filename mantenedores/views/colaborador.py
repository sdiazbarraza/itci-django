from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Colaborador
from ..forms import ColaboradorForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def colaborador_list(request):
	colaborador = Colaborador.objects.all()
	page = Paginator(colaborador, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'colaborador/list.html', {'page': page})

def colaborador_detail(request, pk):
	cargo = get_object_or_404(Colaborador, pk=pk)
	return render(request, 'colaborador/detail.html', {'cargo': cargo})

@login_required
def colaborador_create(request):
	if request.method == "POST":
		form = ColaboradorForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('colaborador_list')
	else:
		form = ColaboradorForm()
	return render(request, 'colaborador/form.html', {'form': form})

@login_required
def colaborador_update(request, pk):
	cargo = get_object_or_404(Colaborador, pk=pk)
	if request.method == "POST":
		form = ColaboradorForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('colaborador_list')
	else:
		form = ColaboradorForm(instance=cargo)
	return render(request, 'colaborador/form.html', {'form': form})

@login_required
@require_POST
def colaborador_delete(request, pk):
	cargo = get_object_or_404(Colaborador, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)