from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class Login(LoginView):
    template_name = "../templates/login.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('rooms') 
        return super().dispatch(request, *args, **kwargs)

class Sign_up(CreateView):
    template_name = "../templates/singUp.html"
    success_url = reverse_lazy('login')