from rest_framework import serializers
from .models import Post, Text
from users.serializers import CustomUserSerializer


class TextSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()

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
        fields = ("id", "slug", "language", "difficulty", "text", "updated", "created")

    # Need to write these methods to allow writable nested fields
    def create(self, validated_data):
        text_data = validated_data.pop("text")
        text = Text.objects.create(**text_data)
        post = Post.objects.create(**validated_data, text=text)
        return post

    def update(self, instance, validated_data):
        text_data = validated_data.pop("text")
        text = instance.text

        instance.id = validated_data.get("id", instance.id)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.language = validated_data.get("language", instance.language)
        instance.difficulty = validated_data.get("difficulty", instance.difficulty)
        instance.updated = validated_data.get("updated", instance.updated)
        instance.created = validated_data.get("created", instance.created)
        instance.save()

        text.id = text_data.get("id", text.id)
        text.title = text_data.get("title", text.title)
        text.original_content = text_data.get("original_content", text.original_content)
        text.author = text_data.get("author", text.author)
        text.is_correction = text_data.get("is_correction", text.is_correction)
        text.is_translation = text_data.get("is_translation", text.is_translation)
        text.save()

        return instance
