from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('books')


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users_login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


