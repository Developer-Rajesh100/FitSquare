from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, RegistrationAPIView, Activate

router = DefaultRouter()
router.register('', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('user/active/<str:uid64>/<str:token>/', Activate.as_view(), name='activate')

]