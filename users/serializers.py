from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "email",
            "level",
            "get_level_display",
            "learning_language",
            "get_learning_language_display",
            "show_notifications",
            "posts",
            "corrected",
        )
