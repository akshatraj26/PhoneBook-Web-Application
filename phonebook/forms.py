from django import forms
from .models import Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'job', 'email', 'label']
        
        
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']