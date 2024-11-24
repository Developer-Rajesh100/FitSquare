from rest_framework import serializers
from .models import Contact

########## Contact Serializer ##########
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['submitted_on',]