from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('contact/', views.create_contact_message, name='create_contact'),
    path('contact/messages/', views.list_contact_messages, name='list_contacts'),
]
