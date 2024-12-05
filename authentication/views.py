from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import quote
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .models import Member
from .serializers import MemberSerializer, RegistrationSerializer, LoginSerializer

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
            token = quote(default_token_generator.make_token(user))
            print(f"token: {token}")
            uid = quote(urlsafe_base64_encode(force_bytes(user.pk)))
            print(f"uid: {uid}")
            confirm_link = f"http://127.0.0.1:8000/member/user/active/{uid}/{token}/"

            # Email Send
            email_subject = "Email Conformation"
            email_body = render_to_string('conformation_email.html', {'conformation_link': confirm_link, 'username': user.username})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({'message': 'Check your email for verification!'})
        return Response(serializer.errors)


class Activate(APIView):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Email Verification Successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Url is not valid'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return Response({"error": "User is not authenticated!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                request.user.auth_token.delete()
            except User.auth_token.RelatedObjectDoesNotExist:
                return Response({"error": "User has no auth_token!"}, status=status.HTTP_400_BAD_REQUEST)
            logout(request)
            return Response({"message": "User logout successfully!"})