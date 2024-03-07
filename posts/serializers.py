from rest_framework import serializers
from .models import Post, Like
from accounts.models import User
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {'username' : UserSerializer(
            User.objects.get(pk=data['user'])).data['username']}
        return data
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'