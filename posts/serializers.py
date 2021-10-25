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
            "get_difficulty_display",
            "language",
            "get_language_display",
            "created",
            "updated",
        )

        extra_kwargs = {
            # "slug": {"required": False, "allow_null": True, "allow_blank": True}
            "slug": {"read_only": True}
        }


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
            "get_difficulty_display",
            "language",
            "get_language_display",
            "is_valid",
            "created",
            "updated",
        )
        extra_kwargs = {"description": {"required": False}}
