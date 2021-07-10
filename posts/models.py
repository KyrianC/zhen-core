from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify


class Text(models.Model):
    """Title and body content of post, content is cut in sentences"""

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


# class Sentence(models.Model):
#     Text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name="sentences")
#     sentence_text = models.CharField(max_length=300)
#     sentence_translation = models.CharField(max_length=600)


class Post(models.Model):
    """Original Post made by user in the language he is practicing"""

    slug = models.SlugField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2, choices=settings.LANGUAGE_CHOICES, default="en"
    )
    difficulty = models.CharField(
        max_length=15, choices=settings.DIFFICULTY_CHOICES, default="beginner"
    )

    def save(self, *args, **kwargs):
        if not self.slug and self.text:
            self.slug = slugify(self.text.title)
        return super().save(*args, **kwargs)


class Correction(models.Model):
    """Corrections of orginal post made by native speaking user"""

    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="corrections", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
