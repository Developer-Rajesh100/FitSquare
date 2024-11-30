from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, RegistrationAPIView

router = DefaultRouter()
router.register('', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/registration/', RegistrationAPIView.as_view(), name='registration'),
]