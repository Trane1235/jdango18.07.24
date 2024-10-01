from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=3000)

    file = models.FileField(upload_to='forum_messages')
    fileText = models.FileField(upload_to='book_content')
    editorial_office = models.CharField(max_length=100)
