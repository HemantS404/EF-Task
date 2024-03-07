from django.urls import path
from knox.views import LogoutView
from .views import RegisterApi, LoginApi, UserUpdateApi

urlpatterns = [
    path('SignUp/', RegisterApi.as_view(), name="signup"),
    path('Login/', LoginApi.as_view(), name='login'),
    path('Update/<pk>/', UserUpdateApi.as_view(), name='update'),
    path('Logout/', LogoutView.as_view(), name='logout'),
]