from django.urls import path

from .views import (create_patient, delete_patient, edit_patient,
                    list_patients, patient_id)

urlpatterns = [
    path('patients/add', create_patient, name='create_patient'),
    path('patients/list', list_patients, name='list_patients'),
    path('patients/<int:pk>', patient_id, name='patient_id'),
    path('patients/<int:pk>/edit',
         edit_patient, name='edit_patient'),
    path('patients/<int:pk>/delete',
         delete_patient, name='delete_patient')
]
