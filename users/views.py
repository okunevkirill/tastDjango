from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializers import CustomUserModelSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
