from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Text(models.Model):
    """Title and body content of post, content(text_data) is cut in sentences, sentences in word, and words with their data(translation, pinyin, etc)"""

    title = models.CharField(max_length=100)
    text_data = models.JSONField(null=True)
    is_correction = models.BooleanField(default=False)
    is_translation = models.BooleanField(default=False)


class Post(models.Model):
    """Original Post made by user in the language he is practicing"""

    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2, choices=settings.LANGUAGE_CHOICES, default="en"
    )
    difficulty = models.CharField(
        max_length=15, choices=settings.DIFFICULTY_CHOICES, default="beginner"
    )


class Correction(models.Model):
    """Corrections of orginal post made by native speaking user"""

    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="corrections", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Translation(models.Model):
    """Translation to add to original post. Can be made by original user or other user if original didn't"""

    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="translations", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
