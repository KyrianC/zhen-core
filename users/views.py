from rest_framework import generics

from django.contrib.auth import get_user_model
from .serializers import UserTextSerializer

User = get_user_model()


class UserTextList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    # TODO make UUID to prevent user enumeration
    lookup_field = "username"
    serializer_class = UserTextSerializer
