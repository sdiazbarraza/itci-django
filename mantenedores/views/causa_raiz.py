from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import CausaRaiz
from ..forms import CausaRaizForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def causa_raiz_list(request):
	causa_raizs = CausaRaiz.objects.all()
	page = Paginator(causa_raizs, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'causa_raiz/list.html', {'page': page})

def causa_raiz_detail(request, pk):
	causa_raiz = get_object_or_404(CausaRaiz, pk=pk)
	return render(request, 'causa_raiz/detail.html', {'causa_raiz': causa_raiz})

@login_required
def causa_raiz_create(request):
	if request.method == "POST":
		form = CausaRaizForm(request.POST)
		if form.is_valid():
			causa_raiz = form.save()
			return redirect('causa_raiz_list')
	else:
		form = CausaRaizForm()
	return render(request, 'causa_raiz/form.html', {'form': form})

@login_required
def causa_raiz_update(request, pk):
	causa_raiz = get_object_or_404(CausaRaiz, pk=pk)
	if request.method == "POST":
		form = CausaRaizForm(request.POST, instance=causa_raiz)
		if form.is_valid():
			form.save()
			return redirect('causa_raiz_list')
	else:
		form = CausaRaizForm(instance=causa_raiz)
	return render(request, 'causa_raiz/form.html', {'form': form})

@login_required
@require_POST
def causa_raiz_delete(request, pk):
	causa_raiz = get_object_or_404(CausaRaiz, pk=pk)
	causa_raiz.delete()
	return JsonResponse({'status': 'success'}, status=200)