from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='users_login'),
    path('register/', views.UserRegisterView.as_view(), name='user_register')
]