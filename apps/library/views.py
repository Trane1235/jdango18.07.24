from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from .models import Book
from . import forms


class BookCreationView(FormView):
    login_url = reverse_lazy('login')
    template_name = 'library/book.html'
    success_url = reverse_lazy('books')
    form_class = forms.NewBook

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        return super().form_valid(form)


class LibraryView(TemplateView):
    template_name = 'library/index.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        context['messages'] = Book.objects.all()
        return super(LibraryView, self).get_context_data(**context)
