from django import forms
from .models import FitnessPlan

class FitnessPlanForm(forms.ModelForm):
    class Meta:
        model = FitnessPlan
        fields = ['name', 'age', 'fitness_level', 'goal', 'duration_weeks', 'workout_schedule']