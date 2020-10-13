from django.urls import path, re_path, register_converter
from .views import login

urlpatterns = [
    path('login', login.login),
]