from rest_framework import generics
from posts import serializers

from posts.models import Post, Correction
from posts.serializers import PostSerializer, CorrectionSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Post.objects.filter(author__username=username)


class UserCorrectionsList(generics.ListAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Correction.objects.filter(author__username=username)


class UserCorrectedList(generics.ListAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Correction.objects.filter(post__author__username=username)
