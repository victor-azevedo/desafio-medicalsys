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
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Usuário e/ou senha inválidos!')
                context = {'form': form}
                return render(request, 'users/login.html', context)

    else:
        form = LoginUserForms()
        context = {'form': form}
        return render(request, 'users/login.html', context)


@anonymous_required
def register(request):
    if request.method == 'POST':
        form = RegisterUserForms(request.POST)

        if form.is_valid():
            name = form['name'].value()
            email = form['email'].value()
            password = form['password'].value()
            password_confirm = form['password_confirm'].value()

            password_redirect = checkPasswordFormOrRedirect(
                request, password, password_confirm)
            if password_redirect:
                return password_redirect

            if User.objects.filter(email=email).exists():
                messages.error(
                    request, f'Email {email} já em uso por outro usuário!')
                context = {'form': form}
                return render(request, 'users/register.html', context)

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
        context = {'form': form}
        return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')


@login_required
def home(request):
    return render(request, 'dashboard.html')


@login_required
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        form = RegisterUserForms(request.POST)

        if form.is_valid():
            name = form['name'].value()
            email = form['email'].value()
            password = form['password'].value()
            password_confirm = form['password_confirm'].value()

            password_redirect = checkPasswordFormOrRedirect(
                request, password, password_confirm)
            if password_redirect:
                return password_redirect

            if User.objects.filter(email=email).exclude(id=user.id).exists():
                messages.error(
                    request, f'Email {email} já em uso por outro usuário!')
                context = {'form': form}
                return render(request, 'users/edit.html', context)

            user.name = name
            user.email = email
            user.set_password(password)
            user.save()
            auth.login(request, user)

            form = RegisterUserForms()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('home')

    else:
        form = RegisterUserForms(
            initial={'name': user.name, 'email': user.email})
        context = {'form': form}
        return render(request, 'users/edit.html', context)


@login_required
def delete_user(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Conta encerrada com sucesso!')
        return redirect('home')

    else:
        return render(request, 'users/delete.html')


def checkPasswordFormOrRedirect(request, password, password_confirm):
    if password != password_confirm:
        messages.error(request, 'Senhas devem ser iguais!')
        return redirect('register')
