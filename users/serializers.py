from rest_framework import serializers
from .models import CustomUser
from posts.models import Text, Correction


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("pk", "username", "email", "level", "learning_language")


class UserCorrectionSerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="posts:detail", lookup_field="slug"
    )

    class Meta:
        model = Correction
        fields = ("is_valid", "post")


class UserTextSerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="posts:detail", lookup_field="slug"
    )
    correction = UserCorrectionSerializer(read_only=True)

    class Meta:
        model = Text
        fields = (
            "id",
            "title",
            "is_correction",
            "is_translation",
            "post",
            "correction",
        )


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
