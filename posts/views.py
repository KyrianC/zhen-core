from rest_framework import generics

from .filters import PostFilter
from .models import Correction, Post
from .permissions import (
    IsAuthorOrReadOnly,
    IsCorrectedAuthorOrReadOnly,
    IsCompetentCorrector,
)
from .serializers import CorrectionSerializer, PostSerializer
from rest_framework.exceptions import ValidationError


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    ordering_fields = ["created"]
    search_fields = ["description", "title", "description", "content"]


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
        post.author = self.request.user
        return super().perform_create(serializer)


class CorrectionCreate(generics.CreateAPIView):
    queryset = Correction.objects.all()
    serializer_class = CorrectionSerializer
    permissions_class = (IsCompetentCorrector,)
    lookup_field = "slug"

    def perform_create(self, serializer):
        correction = serializer.save()
        correction.author = self.request.user
        return super().perform_create(serializer)


class CorrectionDetail(generics.RetrieveUpdateAPIView):
    queryset = Correction.objects.all()
    serializer_class = CorrectionSerializer
    permissions_classes = (IsCorrectedAuthorOrReadOnly, IsAuthorOrReadOnly)
