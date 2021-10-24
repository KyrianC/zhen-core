from rest_framework import serializers
from users.serializers import CustomUserSerializer

from .models import Post, Correction


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    corrections = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="slug"
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "author",
            "corrections",
            "difficulty",
            "language",
            "created",
            "updated",
        )


class CorrectionSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    post = serializers.SlugRelatedField(read_only=True, slug_field="slug")

    class Meta:
        model = Correction
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "author",
            "post",
            "difficulty",
            "language",
            "is_valid",
            "created",
            "updated",
        )
