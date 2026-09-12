from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('agent', views.agent, name='agent'),
    path('services', views.services, name='services'),
]