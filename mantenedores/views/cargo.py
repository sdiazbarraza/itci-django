from django.shortcuts import render, get_object_or_404, redirect
from ..models import Cargo
from ..forms import CargoForm

def index(request):
	return HttpResponse("Hello, this is the Cargo app.")

def cargo_list(request):
	cargos = Cargo.objects.all()
	return render(request, 'cargo/list.html', {'cargos': cargos})

def cargo_detail(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	return render(request, 'cargo/detail.html', {'cargo': cargo})

def cargo_create(request):
	if request.method == "POST":
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			return redirect('cargo_list')
	else:
		form = CargoForm()
	return render(request, 'cargo/form.html', {'form': form})

def cargo_update(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	if request.method == "POST":
		form = CargoForm(request.POST, instance=cargo)
		if form.is_valid():
			cargo = form.save()
			return redirect('cargo_list')
	else:
		form = CargoForm(instance=cargo)
	return render(request, 'cargo/form.html', {'form': form})

def cargo_delete(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	if request.method == "POST":
		cargo.delete()
		return redirect('cargo_list')
	return render(request, 'cargo/confirm_delete.html', {'cargo': cargo})