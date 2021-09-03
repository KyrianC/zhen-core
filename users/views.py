from rest_framework import generics

from .models import CustomUser
from .serializers import UserProfileTextSerializer


class UserTextList(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    # TODO make UUID to prevent user enumeration
    lookup_field = "pk"
    serializer_class = UserProfileTextSerializer
