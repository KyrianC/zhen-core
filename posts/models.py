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
            # decode chinese characters
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ["-updated"]


class Post(Text):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
        null=True,
    )

    @property
    def has_new_corrections(self):
        return self.corrections.filter(seen_by_author=False).exists()

    class Meta:
        unique_together = ["title", "slug", "difficulty"]


class Correction(Text):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="corrections",
        on_delete=models.CASCADE,
        null=True,
    )
    post = models.ForeignKey(Post, related_name="corrections", on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    score = models.PositiveSmallIntegerField(default=0)
    score_comment = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=False)
    seen_by_author = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.difficulty is None:
            self.difficulty = self.post.difficulty
        if self.language is None:
            self.language = self.post.language
        return super().save(*args, **kwargs)

    def make_valid(self):
        """
        make it the one true correction of the post when validated by
        post author
        """
        other_corrections = self.post.corrections.all().exclude(id=self.id)
        for correction in other_corrections:
            correction.is_valid = False
        self.is_valid = True
        self.save()
