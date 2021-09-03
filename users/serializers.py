from rest_framework import serializers
from .models import CustomUser
from posts.models import Text


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("pk", "username", "email", "level", "learning_language")


class UserTextSerializer(serializers.ModelSerializer):
    """
    Serializer to be used in UserProfileTextSerializer only.
    Same to posts.TextSerializer but without the author field
    """

    class Meta:
        model = Text
        fields = ("id", "title", "is_correction", "is_translation")


class UserProfileTextSerializer(serializers.ModelSerializer):
    """
    used to retrieve only texts made by a user,
    current User informations will be in each request anyway (dj rest auth),
    so no need to add it here
    """

    text = UserTextSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ("text",)
