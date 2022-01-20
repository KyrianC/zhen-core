from rest_framework import serializers
from users.serializers import CustomUserSerializer

from .models import Post, Correction


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    corrections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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
            "has_new_corrections",
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

    def validate_score(self, value):
        """score must be a value between 0 and 10"""
        if value > 10:
            raise serializers.ValidationError("Score cannot be above 10")
        return value

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
            "note",
            "score",
            "score_comment",
            "difficulty",
            "get_difficulty_display",
            "language",
            "get_language_display",
            "is_valid",
            "seen_by_author",
            "created",
            "updated",
        )
        extra_kwargs = {"description": {"required": False}}
