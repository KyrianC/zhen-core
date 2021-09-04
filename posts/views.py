from django.core.exceptions import ValidationError
from rest_framework import generics

from .filters import PostFilter
from .models import Post, Text
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostReadOnlySerializer,
    PostSerializer,
    TextDetailSerializer,
    TextSerializer,
)


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(
        text__is_translation=False, text__is_correction=False
    )
    serializer_class = PostReadOnlySerializer
    filterset_class = PostFilter
    ordering_fields = ["created"]
    search_fields = ["description", "text__title", "text__original_content"]


class PostDetail(generics.RetrieveDestroyAPIView):
    permissions_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostReadOnlySerializer
    lookup_field = "slug"


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        post.text.author = self.request.user
        return super().perform_create(serializer)


class TextCorrect(generics.CreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(slug=self.kwargs["slug"])
        if post.author == self.request.user:
            raise ValidationError("You cannot correct your own post")
        # HACK should maybe do it otherwise, maybe make function in models
        if not post.is_correction and post.author.language_learned != post.language:
            raise ValidationError(
                "You can only write in the language you are currently learning"
            )
        elif (
            post.is_correction or post.is_translation
        ) and post.author.language_learned == post.language:
            raise ValidationError(
                "You can only correct or translate content in your native language"
            )
        text = serializer.save(author=self.request.user, is_correction=True, post=post)
        return super().perform_create(serializer)
