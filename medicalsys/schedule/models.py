from django.db import models
from django.utils import timezone
from patients.models import Patient
from users.models import User

TO_CONFIRM = 'TO_CONFIRM'
CONFIRMED = 'CONFIRMED'
FINISHED = 'FINISHED'


class Schedule(models.Model):
    STATUS_CHOICES = [
        (TO_CONFIRM, 'A Confirmar'),
        (CONFIRMED, 'Confirmado'),
        (FINISHED, 'Finalizado'),
    ]

    date = models.DateTimeField()
    description = models.TextField(max_length=1000)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default=TO_CONFIRM)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'D: {self.doctor} - P: {self.patient} - {self.date}'
