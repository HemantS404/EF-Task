from .models import User
from django.contrib.auth import  authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = super().create( validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user