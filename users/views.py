from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.models import Post, Correction
from posts.serializers import PostSerializer, CorrectionSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Post.objects.filter(author__username=username)


class UserCorrectionsList(generics.ListAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Correction.objects.filter(author__username=username)


class UserCorrectedList(generics.ListAPIView):
    serializer_class = CorrectionSerializer

    def get_queryset(self):
        username = self.kwargs.get("username")
        return Correction.objects.filter(post__author__username=username)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unshow_notifications(request):
    user = request.user
    if user.show_notifications == True:
        user.show_notifications = False
        user.save()
    return Response(
        {"show_notifications": user.show_notfications}, status=status.HTTP_200_OK
    )
