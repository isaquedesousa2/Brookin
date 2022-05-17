from django.urls import path
from . import views


urlpatterns = [
    path('entrar', views.login, name='login'),
    path('registrar', views.register, name='register'),
    path('valida_cadastro', views.validate_registration, name='validate_registration'),
    path('valida_entrar', views.validate_login, name='validate_login'),
]
