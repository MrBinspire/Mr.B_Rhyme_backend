from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from home.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=250)
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["id"] = user.id
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class RhymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rhymes
        fields = "__all__"
