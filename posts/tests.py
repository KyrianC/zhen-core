import json
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Post, Text

User = get_user_model()


class PostTest(TestCase):
    text_count = 5

    def setUp(self):
        for i in range(self.text_count):
            user = User.objects.create_user(
                username=f"test{i}", email=f"test{i}@example.com", password="secret"
            )
            text = Text.objects.create(
                title="title", original_content="content", author=user
            )
            Post.objects.create(
                text=text,
                description=f"description{i}",
                language="en",
                difficulty="beginner",
            )
        client = APIClient()

    def test_post_list(self):
        response = self.client.get(reverse("posts:list"), format="json")
        content = json.loads(response.content)
        self.assertEqual(content["count"], self.text_count)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TextTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(self.username, self.email, self.password)
        text = Text.objects.create(
            title="title", original_content="content", author=user
        )
        client = APIClient()
