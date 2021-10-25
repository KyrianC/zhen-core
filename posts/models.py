from django.conf import settings
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Text(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    description = models.CharField(max_length=255)
    content = models.TextField()
    difficulty = models.CharField(
        max_length=15,
        choices=settings.DIFFICULTY_CHOICES,
        default=settings.ENGLISH,
    )
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGE_CHOICES,
        default=settings.ELEMENTARY,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))  # decode chinese characters
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        unique_together = ["title", "slug", "difficulty"]
        ordering = ["-updated"]


class Post(Text):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
        null=True,
    )


class Correction(Text):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="corrections",
        on_delete=models.CASCADE,
        null=True,
    )
    post = models.ForeignKey(Post, related_name="corrections", on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.difficulty is None:
            self.difficulty = post.difficulty
        if self.language is None:
            self.language = post.language
        return super().save(*args, **kwargs)

    def validate(self):
        other_corrections = post.corrections.all().exclude(pk=self.id)
        for correction in other_corrections:
            correction.is_valid = False
        self.is_valid = True
