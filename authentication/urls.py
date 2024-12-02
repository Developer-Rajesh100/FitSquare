from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, RegistrationAPIView, Activate, LoginAPIView, LogoutAPIView

router = DefaultRouter()
router.register('', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('user/logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/active/<str:uid64>/<str:token>/', Activate.as_view(), name='activate')

]