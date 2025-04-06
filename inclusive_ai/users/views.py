from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginUser(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('initiatives')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('initiatives')


def logout_user(request):
    logout(request)
    return redirect('homepage')
