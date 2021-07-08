from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone',
            'password'
        )