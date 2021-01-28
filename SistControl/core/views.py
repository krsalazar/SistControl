from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
"""Esta vista va a permitir redireccionar a una página personalizada al usuario que no tenga
los permisos requeridos para visualizar ciertas áreas, se va a heredar en otras vistas"""
class SinAcceso(LoginRequiredMixin ,PermissionRequiredMixin):
    login_url = 'core:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        if not self.request.user == AnonymousUser():
            self.login_url = 'core:denegado'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin ,generic.TemplateView):
    template_name = 'core/home.html'
    login_url = 'core:login'

"""Con este mixin le indicamos que para tener acceso a esta vista, debemos
estar autenticados como usuario, que depende de la url login"""

class Denegado(generic.TemplateView):
    template_name = 'core/403.html'