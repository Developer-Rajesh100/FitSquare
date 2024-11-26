from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Member
        fields = '__all__'