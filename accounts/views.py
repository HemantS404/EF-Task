from django.contrib.auth import login
from .models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from knox.views import LoginView
from rest_framework.permissions import IsAuthenticated

class RegisterApi(CreateAPIView):
    serializer_class = UserSerializer

class LoginApi(LoginView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if not serializer.is_valid():
                return Response(f'Some error has occured : {serializer.errors}')
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApi, self).post(request, format=None)  

class UserUpdateApi(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects