from django.urls import path

from .views import create_patient, list_patients

urlpatterns = [
    path('patients/add', create_patient, name='create_patient'),
    path('patients/list', list_patients, name='list_patients'),
]
