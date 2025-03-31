from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import FitnessPlan
from .forms import FitnessPlanForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Sample data (normally from the database)
items = ["Item 1", "Item 2", "Item 3"]

def item_list(request):
    """Render main template with items."""
    return render(request, "index.html", {"items": items})

def load_items(request):
    """Return partial HTML for item list."""
    return render(request, "partials/item_list.html", {"items": items})

# Add this view if you want to render the fitness plan list for the root URL
def index(request):
    return redirect('fitnessplan_list')  # Redirect to the fitnessplan_list page

@csrf_exempt  # Only for demo; use CSRF tokens in production
def add_item(request):
    """Handle item creation."""
    if request.method == "POST":
        new_item = request.POST.get("item", "New Item")
        items.append(new_item)
        return load_items(request)  # Return updated list

@csrf_exempt
def delete_item(request, index):
    """Handle item deletion."""
    if request.method == "DELETE":
        try:
            items.pop(int(index))
        except IndexError:
            pass  # Handle invalid index case
        return load_items(request)

@csrf_exempt
def update_item(request, index):
    """Handle item update."""
    if request.method == "PUT":
        updated_item = request.POST.get("item", f"Updated Item {index}")
        try:
            items[int(index)] = updated_item
        except IndexError:
            pass
        return load_items(request)

def my_partial_view(request):
    from datetime import datetime
    return render(request, "partials/my_partial.html", {"message": "Hello from HTMX!" f"Current time: {datetime.now()}"})

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

class FitnessPlanDeleteView(DeleteView):
    model = FitnessPlan
    template_name = "fitnessplan_confirm_delete.html"
    success_url = reverse_lazy('fitnessplan_list')  # Redirect after deletion


