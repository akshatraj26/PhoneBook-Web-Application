from django.urls import path
from .views import index, contact_list ,new_contact, contact_detail, delete_contact, update_contact, edit_profile, ContactView, about_me, profile

urlpatterns = [
    path('', index, name='home'),
    path('phonebook/list', contact_list, name='contact-list'),
    path('phonebook/create', new_contact, name='add-contact'),
    path('phonebook/details/<int:pk>/', contact_detail, name='contact-detail'),
    path('phonebook/delete/<int:pk>/', delete_contact, name='delete-contact'),
    path('phonebook/update/<int:pk>/', update_contact, name='update-contact'),
    path('phonebook/contact_me/', ContactView.as_view(), name='contact'),
    path('phonebook/about_me/', about_me, name='about-me'),
    path('phonebook/profile/', profile, name='profile'),
    path('phonebook/profile/edit-profile', edit_profile, name='edit_profile'),
]
