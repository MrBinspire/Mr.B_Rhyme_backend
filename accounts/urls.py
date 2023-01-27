from django.urls import path 
from .api import *
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('auth/register', RegisterApi.as_view()),
    path('auth/login', MyTokenObtainPairView.as_view()),
    path('auth/login-refresh',TokenRefreshView.as_view()),
]
