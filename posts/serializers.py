from rest_framework import serializers
from .models import Post, Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = (
            "id",
            "title",
            "original_content",
            "author",
            "is_correction",
            "is_translation",
        )


class PostSerializer(serializers.ModelSerializer):
    text = TextSerializer()

    class Meta:
        model = Post
        depth = 3
        fields = ("id", "slug", "language", "text", "updated", "created")

    def create(self, validated_data):
        text_data = validated_data.pop("text")
        text = Text.objects.create(**text_data)
        post = Post.objects.create(**validated_data, text=text)
        return post
