from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from users.forms import LoginUserForms, RegisterUserForms

from .models import User


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.HOME_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url,
        redirect_field_name=None
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


@anonymous_required
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
                return redirect('home')
            else:
                messages.error(request, 'Usuário e/ou senha inválidos!')
                return redirect('login')

    else:
        form = LoginUserForms()
        return render(request, 'users/login.html', {'form': form})


@anonymous_required
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


@login_required
def home(request):
    return render(request, 'dashboard.html')
