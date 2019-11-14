from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.fn_login),
    path('register/',views.fn_register),
   
]