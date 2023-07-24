from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PatientForm
from .models import Patient


@login_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            form = PatientForm()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('list_patients')

    else:
        form = PatientForm()
        context = {'form': form}
        return render(request, 'patients/add.html', context)


@login_required
def list_patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patients/list.html', context)


@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            form = PatientForm()
            messages.success(request, 'Paciente atualizado com sucesso!')
            return redirect('list_patients')

    else:
        form = PatientForm(instance=patient)
        context = {'form': form, 'patient': patient}
        return render(request, 'patients/edit.html', context)


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)

    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Paciente deletado com sucesso!')
        return redirect('list_patients')

    else:
        context = {'patient': patient}
        return render(request, 'patients/delete.html', context)
