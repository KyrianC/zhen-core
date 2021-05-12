from rest_framework import serializers
from .models import Text, Post, Sentence, Translation, Correction


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 3
        fields = ("id", "slug", "language", "text", "updated", "created")
