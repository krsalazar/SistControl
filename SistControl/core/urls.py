from django.urls import path
from .views import Home, Denegado
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name='home'),
#Esta es otra forma de configurar las URL para busqueda inversa
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),
    path('denegado/', Denegado.as_view(), name='denegado'),
]
