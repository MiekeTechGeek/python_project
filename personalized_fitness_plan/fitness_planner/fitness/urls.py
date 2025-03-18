from django.urls import path
from . import views

urlpatterns = [
    path('fitnessplans/', views.fitnessplan_list, name='fitnessplan_list'),
    path('fitnessplans/create/', views.fitnessplan_create, name='fitnessplan_create'),
    path('fitnessplans/update/<int:pk>/', views.fitnessplan_update, name='fitnessplan_update'),
    path('fitnessplans/delete/<int:pk>/', views.fitnessplan_delete, name='fitnessplan_delete'),
]