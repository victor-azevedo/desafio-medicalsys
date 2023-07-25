from django import forms

from .models import Schedule
from .utils import current_datetime_str


class ScheduleForm(forms.ModelForm):
    date = forms.DateTimeField(label='Data', input_formats='%Y-%m-%dT%H:%M', widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control', 'min': current_datetime_str}))

    class Meta:
        model = Schedule
        exclude = ['created_at']
        widgets = {
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

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        initial_date = self.instance.date
        if initial_date:
            self.initial['date'] = initial_date.strftime("%Y-%m-%dT%H:%M")
