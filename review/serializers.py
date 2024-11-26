from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'