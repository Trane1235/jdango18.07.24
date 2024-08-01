from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserRegisterFrom
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    from_class = UserRegisterFrom
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


