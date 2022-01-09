from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
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
        )


# class UserCorrectionsSerializer(serializers.ModelSerializer):
#     # import here to avoid circular import with posts.serializers
#     from posts.serializers import CorrectionSerializer

#     corrections = CorrectionSerializer(read_only=True, many=True)

#     class Meta:
#         model = User
#         fields = ("corrections",)


# class UserPostSerializer(serializers.ModelSerializer):
#     # import here to avoid circular import with posts.serializers
#     from posts.serializers import PostSerializer

#     posts = PostSerializer(read_only=True, many=True)

#     class Meta:
#         model = User
#         fields = ("posts",)
