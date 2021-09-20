from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser
from posts.models import Text, Post
from .serializers import UserProfileTextSerializer

User = get_user_model()


class CustomUserTest(TestCase):
    username = "John"
    password = "S3cr37"
    email = "john@example.com"

    def setUp(self):
        user = User.objects.create_user(self.username, self.email, self.password)
        text = Text.objects.create(
            title="title", original_content="content", author=user
        )
        client = APIClient()

    def test_uncomplete_user_profile(self):
        """
        when user first register, they don't set
        level and learning_language directly
        """
        user = User.objects.get(username=self.username)
        self.assertEqual(user.level, "unset")
        self.assertEqual(user.learning_language, "unset")

    def test_get_user_texts(self):
        user = User.objects.get(username="John")
        serializer = UserProfileTextSerializer(user)
        response = self.client.get(reverse("users:texts", kwargs={"pk": user.pk}))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
