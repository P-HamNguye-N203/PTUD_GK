from rest_framework import serializers

from .models import User, Phone

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('name','phoneNumber')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']