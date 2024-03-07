from rest_framework import serializers
from .models import Connection
from accounts.models import User
from accounts.serializers import UserSerializer

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['from_user'] = {'username' : UserSerializer(
            User.objects.get(pk=data['from_user'])).data['username']}
        data['to_user'] = {'username' : UserSerializer(
            User.objects.get(pk=data['to_user'])).data['username']}
        return data
    
class SuggestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio')