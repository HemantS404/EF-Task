from django.shortcuts import render
from .models import Post, Like
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, DestroyAPIView
from .serializers import PostSerializer, LikeSerializer
from rest_framework.response import Response

# Create your views here.
class PostApi(ListAPIView, GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects

    def post(self, request):
        serializer = self.serializer_class(data = {'user':request.user.id, 'description': request.data.get('description')})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class LikeApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects

    def post(self, request):
        serializer = self.serializer_class(data = {'user':request.user.id, 'post': request.data.get('post')})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class UnLikeApi(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects

    def post(self, request):
        try:
            instance = self.queryset.get(user = request.user.id, post = request.data.get('post'))
            instance.delete()
            return Response("User Unliked the post")
        except:
            return Response("User haven't liked the post")
        
