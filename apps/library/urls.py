from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookCreationView.as_view(), name='new_book'),
    path('', views.LibraryView.as_view(), name='books'),
]
