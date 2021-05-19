from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post, Text


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # TODO add filter and pagination


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """add request.user as text author"""
        post = serializer.save()
        post.text.author = self.request.user
        return super().perform_create(serializer)
