from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Merma
from ..forms import MermaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def merma_list(request):
	merma = Merma.objects.all()
	page = Paginator(merma, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'merma/list.html', {'page': page})

def merma_detail(request, pk):
	cargo = get_object_or_404(Merma, pk=pk)
	return render(request, 'merma/detail.html', {'cargo': cargo})

@login_required
def merma_create(request):
	if request.method == "POST":
		form = MermaForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('merma_list')
	else:
		form = MermaForm()
	return render(request, 'merma/form.html', {'form': form})

@login_required
def merma_update(request, pk):
	cargo = get_object_or_404(Merma, pk=pk)
	if request.method == "POST":
		form = MermaForm(request.POST, instance=cargo)
		if form.is_valid():
			form.save()
			return redirect('merma_list')
	else:
		form = MermaForm(instance=cargo)
	return render(request, 'merma/form.html', {'form': form})

@login_required
@require_POST
def merma_delete(request, pk):
	cargo = get_object_or_404(Merma, pk=pk)
	cargo.delete()
	return JsonResponse({'status': 'success'}, status=200)