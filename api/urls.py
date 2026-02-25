from django.urls import path
from api import views

urlpatterns = [
    path('sync/', views.contador_sincrono, name='contador_sincrono'),
    path('async/', views.contador_assincrono, name='contador_assincrono'),
]
