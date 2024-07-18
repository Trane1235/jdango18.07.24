from django.urls import path
from . import views

urlpatterns = [
    path('forum', views.forum, name='forum_index'),
    path('new', views.new_form, name='new_message'),
]
