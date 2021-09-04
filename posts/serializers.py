from rest_framework import serializers
from users.serializers import CustomUserSerializer

from .models import Post, Text


# NOTE using two text serializers: one with user custom serializer and one
# without, then two post serializers who will take each text serializers
# so customUserSerializer will be present only on readonly views


class TextDetailSerializer(serializers.ModelSerializer):
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


class PostReadOnlySerializer(serializers.ModelSerializer):
    text = TextDetailSerializer()

    class Meta:
        model = Post
        depth = 3
        fields = (
            "id",
            "slug",
            "language",
            "difficulty",
            "description",
            "text",
            "updated",
            "created",
        )


class TextSerializer(serializers.ModelSerializer):
    """
    To use only with with PostSerializer, otherwise if we use
    CustomUserSerializer for the author field it will try to create
    a user at the same time as the post & text and I don't know
    how to prevent that
    """

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
        fields = (
            "id",
            "slug",
            "language",
            "difficulty",
            "description",
            "text",
            "updated",
            "created",
        )

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
        instance.description = validated_data.get("description", instance.description)
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
