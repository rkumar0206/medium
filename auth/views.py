from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from auth.serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from auth.serializers import RegisterSerializer
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

