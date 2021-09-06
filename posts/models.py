from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify


class Text(models.Model):
    """only the Title and content of post/correction/translation"""

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="text",
        on_delete=models.CASCADE,
        null=True,
    )
    original_content = models.TextField(null=True)
    is_correction = models.BooleanField(default=False)
    is_translation = models.BooleanField(default=False)
    # post (optional)
    # correction (optional)
    # translation (optional)


class Post(models.Model):
    """Original Post made by user in the language he is practicing"""

    slug = models.SlugField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="post description")
    language = models.CharField(
        max_length=2, choices=settings.LANGUAGE_CHOICES, default="en"
    )
    difficulty = models.CharField(
        max_length=15, choices=settings.DIFFICULTY_CHOICES, default="beginner"
    )
    # corrections

    def save(self, *args, **kwargs):
        if not self.slug and self.text:
            self.slug = slugify(self.text.title, allow_unicode=True)
        return super().save(*args, **kwargs)


class Correction(models.Model):
    """Corrections of orginal post made by native speaking user"""

    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="corrections", on_delete=models.CASCADE)
    is_valid = models.BooleanField(
        default=False
    )  # to be validated by original author or a 3rd user
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
