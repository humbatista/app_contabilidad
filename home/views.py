from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Home(LoginRequiredMixin, View):
    Login_url = '/usuarios/login'
    redirect_field_name = None

    def get(self, request):
        template_name = 'home/inicio.html'
        contexto={}
        return render(request, template_name, contexto)
