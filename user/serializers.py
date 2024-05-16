from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model


EXISITING_EMAIL_ERROR = "Email already exist"

class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserSignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "password",
            "firstname",
            "lastname",
            "created_at",
            "updated_at",
            "is_active",
        ]

    def validate(self, attrs):
        email = attrs.get("email", None)
        if email:
            email = attrs["email"].lower().strip()
            if get_user_model().objects.filter(email=email).exists():
                raise serializers.ValidationError("Email already exists")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
