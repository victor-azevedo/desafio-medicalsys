from django.db import models
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField('patient name', max_length=100)
    phone = models.CharField('phone number', max_length=15)
    address = models.CharField('address', max_length=255)
    address_number = models.CharField('address number', max_length=100)
    city = models.CharField('city', max_length=100)
    uf = models.CharField('UF', max_length=2)
    country = models.CharField('country', max_length=100)
    cep = models.CharField('CEP', max_length=9)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
