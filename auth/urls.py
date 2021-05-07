from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from auth.views import RegisterView, UpdateUserView, ChangePasswordView, LogoutView, LogoutAllView
from django.urls import path

# We previously changed the token obtain url to add custom claim. 
# But blacklist app not compatible with custom claim. 
# For this reason, we’ll change urls.py and we’ll use default views.


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/', RegisterView.as_view(), name = 'auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name = 'auth_change_password'),
    path('update_profile/<int:pk>/', UpdateUserView.as_view(), name = 'auth_update_profile'),
    path('logout/', LogoutView.as_view(), name = 'auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name = 'auth_logout_all'),
]
