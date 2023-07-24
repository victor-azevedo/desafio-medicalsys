from django.urls import path

from .views import (create_schedule, delete_schedule, edit_schedule,
                    list_schedules)

urlpatterns = [
    path('schedule/add', create_schedule, name='create_schedule'),
    path('schedule/list', list_schedules, name='list_schedules'),
    path('schedule/<int:pk>/edit',
         edit_schedule, name='edit_schedule'),
    path('schedule/<int:pk>/delete',
         delete_schedule, name='delete_schedule')
]
