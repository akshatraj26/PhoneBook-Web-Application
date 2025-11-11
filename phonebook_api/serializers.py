from rest_framework import serializers
from phonebook.models import Contact, ContactMe

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        
    