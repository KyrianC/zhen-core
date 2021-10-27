from rest_framework import generics

from posts.models import Post, Correction
from posts.serializers import PostSerializer, CorrectionSerializer


class UserPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    lookup_field = "username"
    serializer_class = PostSerializer


class UserCorrectionsList(generics.ListAPIView):
    queryset = Correction.objects.all()
    lookup_field = "username"
    serializer_class = CorrectionSerializer
