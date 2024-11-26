from django.shortcuts import render
from rest_framework import viewsets
from .models import Classes
from .serializers import ClassesSerializer

# Create your views here.
class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer