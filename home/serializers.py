from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials Passed.")


class RhymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rhymes
        fields = "__all__"


class WordOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOfTheDay
        fields = "__all__"

class AcceptedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accepted
        fields = "__all__"
