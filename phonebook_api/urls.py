from django.urls import path
from .views import getContact

urlpatterns = [
    path("", getContact, name = 'api-contact')
]
