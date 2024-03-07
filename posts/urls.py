from django.urls import path

from .views import PostApi, LikeApi, UnLikeApi

urlpatterns = [
    path('Post/', PostApi.as_view(), name="post"),
    path('Like/', LikeApi.as_view(), name="like"),
    path('UnLike/', UnLikeApi.as_view(), name="unlike"),
]