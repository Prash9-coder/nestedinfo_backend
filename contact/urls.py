from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.create_contact_message, name='create_contact'),
    path('contact/messages/', views.list_contact_messages, name='list_contacts'),
]
