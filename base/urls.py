from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('agent', views.agent, name='agent'),
    path('services', views.services, name='services'),
    path('contact', views.contacts, name='contacts'),
    path('properties', views.properties, name='properties'),
    path('properties/<int:pk>', views.property_details, name='property_details'),
    # path('add-house', views.add_house, name='add_house'),
    path('add-house', views.HouseView.as_view(), name='add_house'),
    path('basket', views.BasketView.as_view(), name='basket'),
    path('api/update-count', views.update_count, name='update_count')
]
