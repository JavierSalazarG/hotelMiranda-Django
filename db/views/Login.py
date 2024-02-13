from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect

class Login(LoginView):
    template_name = "../templates/login.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('rooms') 
        return super().dispatch(request, *args, **kwargs)