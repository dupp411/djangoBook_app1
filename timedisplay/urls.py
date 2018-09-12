from django.urls import path
from .views import current_time, hours_ahead

urlpatterns = [
    path('plus/<int:hour_diff>',hours_ahead,name='hours_ahead'),
    path('',current_time, name = 'current_time'),
]