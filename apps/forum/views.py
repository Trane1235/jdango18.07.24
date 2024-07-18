from django.shortcuts import render, redirect
from django.http import HttpRequest
from . import forms


def new_form(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {
            'form': forms.ForumMessageForm
        }
        return render(request, 'users/login.html', template_kwargs)

    # Добавление нового сообщение сделать тут
    return redirect(index)




def forum(request: HttpRequest):
    template_kwargs = {
        'user': request.user,

    }
    return render(request, 'forum/forum.html', template_kwargs)
