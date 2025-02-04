from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Turno
from ..forms import TurnoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def turno_list(request):
	turno = Turno.objects.all()
	page = Paginator(turno, 10)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)

	return render(request, 'turno/list.html', {'page': page})

def turno_detail(request, pk):
	turno = get_object_or_404(Turno, pk=pk)
	return render(request, 'turno/detail.html', {'turno': turno})

@login_required
def turno_create(request):
	if request.method == "POST":
		form = TurnoForm(request.POST)
		if form.is_valid():
			turno = form.save()
			return redirect('turno_list')
	else:
		form = TurnoForm()
	return render(request, 'turno/form.html', {'form': form})

@login_required
def turno_update(request, pk):
	turno = get_object_or_404(Turno, pk=pk)
	if request.method == "POST":
		form = TurnoForm(request.POST, instance=turno)
		if form.is_valid():
			form.save()
			return redirect('turno_list')
	else:
		form = TurnoForm(instance=turno)
	return render(request, 'turno/form.html', {'form': form})

@login_required
@require_POST
def turno_delete(request, pk):
	turno = get_object_or_404(Turno, pk=pk)
	turno.delete()
	return JsonResponse({'status': 'success'}, status=200)