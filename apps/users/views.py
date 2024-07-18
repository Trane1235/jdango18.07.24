from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest
from django.contrib import messages
import django.contrib.auth as auth
from . import forms
import datetime


def login(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {
            'form': forms.LoginForm
        }
        return render(request, 'users/login.html', template_kwargs)

    login_form = forms.LoginForm(request.POST)
    if not login_form.is_valid():
        pass
    password = request.POST.get('password')
    username = request.POST.get('username')
    user = auth.authenticate(request, password=password, username=username)

    if user is None:
        messages.info(request, 'Неверный логин или пароль')
        return redirect(login)

    else:
        auth.login(request, user)
        return redirect(reverse('forum_index'))


def register(request: HttpRequest):
    if request.method == "GET":
        template_kwargs = {'form': forms.RegisterForm}
        return render(request, 'users/register.html', template_kwargs )

    register_form = forms.RegisterForm(request.POST)
    if not register_form.is_valid():
        messages.info(request, register_form.errors)
        return redirect(register)


    user = register_form.save()
    user.set_password(register_form.cleaned_data.get("password"))
    user.save()
    return redirect(login)


def get_time(request: HttpRequest):
    curr_time = datetime.datetime.now()
    template_kwargs = {
        "time": curr_time.time(),
        "date": curr_time.date()
    }
    return render(request, 'time.html', template_kwargs)

