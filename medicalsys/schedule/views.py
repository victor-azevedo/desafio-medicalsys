from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ScheduleForm


@login_required
def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            form.save()
            form = ScheduleForm()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Dados inválidos!')
            context = {'form': form}
            return render(request, 'schedule/add.html', context)

    else:
        form = ScheduleForm()
        context = {'form': form}
        return render(request, 'schedule/add.html', context)
