from django.contrib import auth, messages
from django.shortcuts import redirect, render
from users.forms import LoginUserForms, RegisterUserForms

from .models import User


def login(request):
    if request.method == 'POST':
        form = LoginUserForms(request.POST)

        if form.is_valid():
            email = form['email'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                email=email,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('login')
            else:
                messages.error(request, 'Usuário e/ou senha inválidos!')
                return redirect('login')

    else:
        form = LoginUserForms()
        return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForms(request.POST)

        if form.is_valid():
            if form["password"].value() != form["password_confirm"].value():
                messages.error(request, 'Senhas devem ser iguais!')
                return redirect('register')

            name = form['name'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Usuário já existente!')
                return redirect('register')

            user = User.objects.create_user(
                name=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    else:
        form = RegisterUserForms()
        return render(request, 'users/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
