from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# User = get_user_model()

class Contact(models.Model):
    EXCURSIONS = (
        ('mobile', 'Mobile'),
        ('work', 'Work'),
        ('home', 'Home'),
        ('friends', 'Friends'),
        ('others', 'Others'),
    )
    
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(region = 'IN')
    job = models.CharField(max_length=256, null=True)
    email = models.EmailField(null=True)
    label = models.CharField(max_length=100, choices=EXCURSIONS)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'phone')
    
    def __str__(self):
        return f"{self.name}| {self.job}"
    
    
class ContactMe(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} | {self.email}"