from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PatientForm
from .models import Patient


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            form = PatientForm()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('home')

    else:
        form = PatientForm()
        context = {'form': form}
        return render(request, 'patients/add.html', context)


def list_patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patients/list.html', context)
