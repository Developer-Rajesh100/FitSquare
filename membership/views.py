from django.shortcuts import render
from rest_framework import viewsets
from .models import Membership
from .serializers import MembershipSerializer

# Create your views here.
class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer