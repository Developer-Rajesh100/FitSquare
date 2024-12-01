from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer, RegistrationSerializer

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)

            # Token Setup
            token = default_token_generator.make_token(user)
            print(f"token: {token}")
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(f"uid: {uid}")
            confirm_link = f"http://127.0.0.1:8000/member/user/active{uid}/{token}"

            # Email Send
            email_subject = "Email Conformation"
            email_body = render_to_string('conformation_email.html', {'conformation_link': confirm_link, 'username': user.username})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({'message': 'Check your email for verification!'})
        return Response(serializer.errors)
