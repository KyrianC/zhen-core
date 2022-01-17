from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from django.core.exceptions import ObjectDoesNotExist

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
        post = serializer.save(author=self.request.user)
        return super().perform_create(serializer)


# BUG difficulty not set properly
class CorrectionCreate(generics.CreateAPIView):
    queryset = Correction.objects.all()
    serializer_class = CorrectionSerializer
    permissions_class = (IsCompetentCorrector,)
    lookup_field = "slug"

    def perform_create(self, serializer):
        author = self.request.user
        slug = self.kwargs["slug"]
        post = Post.objects.get(slug=slug)
        correction = serializer.save(
            author=author,
            post=post,
            description=post.description,
            language=post.language,
            difficulty=post.difficulty,
        )
        return super().perform_create(serializer)


@api_view(["POST"])
def validate_correction(request, correction_id):
    print(correction_id)
    try:
        correction = Correction.objects.get(id=correction_id)
    except ObjectDoesNotExist:
        return Response(
            {"not_found": "error: post or correction not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    post = correction.post
    if post.author != request.user:
        return ValidationError("You cannot validate other users posts")
    correction.make_valid()
    return Response({"is_valid": correction.is_valid}, status=status.HTTP_200_OK)


class CorrectionDetail(generics.RetrieveUpdateAPIView):
    queryset = Correction.objects.all()
    serializer_class = CorrectionSerializer
    permissions_classes = (IsCorrectedAuthorOrReadOnly, IsAuthorOrReadOnly)
    lookup_field = "slug"


class PostCorrectionList(generics.ListAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        post = self.kwargs.get("post_slug")
        return Correction.objects.filter(post__slug=post)
