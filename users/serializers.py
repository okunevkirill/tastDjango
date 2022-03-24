from rest_framework import serializers

from .models import CustomUser


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)
