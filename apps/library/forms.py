from .models import Book
from django import forms


class NewBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('editorial_office', 'author', 'name', 'description', 'file', 'fileText')
