from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "email", "level", "learning_language")


class UserTextSerializer(serializers.ModelSerializer):
    # import here to avoid circular import with posts.serializers
    from posts.serializers import PostSerializer, CorrectionSerializer

    posts = PostSerializer(read_only=True, many=True)
    corrections = CorrectionSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ("posts", "corrections")
