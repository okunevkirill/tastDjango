"""
tastDjango URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
