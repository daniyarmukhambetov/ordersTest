from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField(
        required=True,
        min_length=3,
        max_length=255,
    )
    password = serializers.CharField(
        required=False,
        min_length=8,
        max_length=64,
        write_only=True,
    )

    @extend_schema_field(OpenApiTypes.STR)
    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "token",
        ]

    def validate(self, attrs):
        user = User.objects.filter(email=attrs.get("email"))
        if user.exists():
            raise serializers.ValidationError(f"user with email {user[0].email} is already exists")
        return super(UserSerializer, self).validate(attrs)


class UserLoginSerializer(UserSerializer):
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = User.objects.filter(
            email=email
        ).first()
        if user is None:
            raise serializers.ValidationError(
                "user not found"
            )
        if not user.is_active:
            raise serializers.ValidationError(
                "user is not active"
            )
        # print(user.password)
        if user.password != password:
            raise serializers.ValidationError(
                "invalid password"
            )
        self.instance = user
        return data
