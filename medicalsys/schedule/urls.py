from django.urls import path

from .views import create_schedule

urlpatterns = [
    path('schedule/add', create_schedule, name='create_schedule'),
]
