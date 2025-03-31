from django.urls import path
from . import views
from .views import FitnessPlanDeleteView, fitnessplan_delete, fitnessplan_list, fitnessplan_update, my_partial_view
from .views import fitnessplan_create

urlpatterns = [
    path('', views.index, name='home'),  # Add this line for the root URL
    path('fitnessplans/', fitnessplan_list, name='fitnessplan_list'),
    path('fitnessplans/create/', fitnessplan_create, name='fitnessplan_create'),
    path('fitnessplan/<int:pk>/edit/', fitnessplan_list, name='fitnessplan_edit'),
    path('fitnessplans/update/<int:pk>/', fitnessplan_update, name='fitnessplan_update'),
    path('fitnessplans/delete/<int:pk>/', fitnessplan_delete, name='fitnessplan_delete'),
    path('fitnessplan/<int:pk>/delete/', FitnessPlanDeleteView.as_view(), name='fitnessplan_confirm_delete'),
    path('my-partial/', my_partial_view, name='my_partial'),
]
