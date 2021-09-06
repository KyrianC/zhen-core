from django.core.exceptions import ValidationError
from rest_framework import generics

from .filters import PostFilter
from .models import Post, Text, Correction
from .permissions import IsAuthorOrReadOnly, IsCorrectedAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    TextSerializer,
    CorrectionSerializer,
)


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(
        text__is_translation=False, text__is_correction=False
    )
    serializer_class = PostSerializer
    filterset_class = PostFilter
    ordering_fields = ["created"]
    search_fields = ["description", "text__title", "text__original_content"]


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


class TextCorrect(generics.CreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        post = Post.objects.get(slug=self.kwargs["slug"])
        original_text = post.text
        if original_text.author == self.request.user:
            raise ValidationError("You cannot correct your own post")
        # HACK should maybe do it otherwise, maybe make function in models
        if (
            not original_text.is_correction
            and original_text.author.learning_language != post.language
        ):
            raise ValidationError(
                "You can only write in the language you are currently learning"
            )
        elif (
            original_text.is_correction or original_text.is_translation
        ) and original_text.author.learning_language == post.language:
            raise ValidationError(
                "You can only correct or translate content in your native language"
            )
        text = serializer.save(author=self.request.user, is_correction=True)
        correction = Correction.objects.create(text=text, post=post)

        return super().perform_create(serializer)


class TextCorrectionDetail(generics.RetrieveUpdateAPIView):
    queryset = Correction.objects.all()
    serializer_class = CorrectionSerializer
    permissions_classes = (IsCorrectedAuthorOrReadOnly,)
