from django import forms

from .models import Schedule


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ['created_at']
        widgets = {
            'date': DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Date',
            'description': 'Descrição',
            'status': 'Status',
            'doctor': 'Médico',
            'patient': 'Paciente',
        }
