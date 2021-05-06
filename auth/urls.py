from rest_framework_simplejwt.views import TokenRefreshView
from auth.views import MyObtainTokenPairView, RegisterView
from django.urls import path

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/', RegisterView.as_view(), name = 'auth_register'),
]