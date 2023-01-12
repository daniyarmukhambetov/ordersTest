from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    def validate(self, attrs):
        return super(ProfileSerializer, self).validate(attrs)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "telephone", "user"]

    def create(self, validated_data):
        if self.context.get("request").user.user_profile is not None:
            raise serializers.ValidationError("this user already has profile")
        return super(ProfileSerializer, self).create(validated_data)