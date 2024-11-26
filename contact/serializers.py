from rest_framework import serializers
from .models import Contact

########## Contact Serializer ##########
class ContactSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField(many=False)
    class Meta:
        model = Contact
        fields = '__all__'