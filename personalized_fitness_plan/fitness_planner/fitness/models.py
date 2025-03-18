from django.db import models

# Create your models here.
class FitnessPlan(models.Model):
    FITNESS_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    fitness_level = models.CharField(max_length=20, choices=FITNESS_LEVELS)
    goal = models.CharField(max_length=255, help_text="E.g., Weight Loss, Muscle Gain, Endurance")
    duration_weeks = models.IntegerField(help_text="Duration in weeks")
    workout_schedule = models.TextField(help_text="Describe weekly workout plan")

    def __str__(self):
        return f"{self.name} - {self.goal} ({self.fitness_level})"