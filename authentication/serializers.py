from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'email', 'password', 'is_superuser', 'is_staff', 'groups',
            'user_permissions'
        ]
