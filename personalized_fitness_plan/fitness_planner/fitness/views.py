from django.shortcuts import render, redirect, get_object_or_404
from .models import FitnessPlan
from .forms import FitnessPlanForm

# Create your views here.
def fitnessplan_list(request):
    plans = FitnessPlan.objects.all()
    return render(request, 'fitnessplan_list.html', {'plans': plans})

def fitnessplan_create(request):
    if request.method == 'POST':
        form = FitnessPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitnessplan_list')
    else:
        form = FitnessPlanForm()
    return render(request, 'fitnessplan_form.html', {'form': form})

def fitnessplan_update(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk)
    if request.method == 'POST':
        form = FitnessPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('fitnessplan_list')
    else:
        form = FitnessPlanForm(instance=plan)
    return render(request, 'fitnessplan_form.html', {'form': form})

def fitnessplan_delete(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('fitnessplan_list')
    return render(request, 'fitnessplan_confirm_delete.html', {'plan': plan})