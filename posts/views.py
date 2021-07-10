from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer, TextSerializer
from .models import Post, Text
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(
        text__is_translation=False, text__is_correction=False
    )
    serializer_class = PostSerializer
    # TODO add filter and pagination


class PostDetail(generics.RetrieveDestroyAPIView):
    permissions_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        post.text.author = self.request.user
        return super().perform_create(serializer)


class PostCorrect(generics.CreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(slug=self.kwargs["slug"])
        if post.author == self.request.user:
            raise ValidationError("You cannot correct your own post")
        text = serializer.save(author=self.request.user, is_correction=True, post=post)
        return super().perform_create(serializer)
