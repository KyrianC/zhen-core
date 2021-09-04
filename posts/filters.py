from django.conf import settings

from django_filters import MultipleChoiceFilter, BooleanFilter
from django_filters import rest_framework as filters
from django_filters.fields import CSVWidget

from .models import Post


class PostFilter(filters.FilterSet):
    language = MultipleChoiceFilter(choices=settings.LANGUAGE_CHOICES, widget=CSVWidget)
    difficulty = MultipleChoiceFilter(
        choices=settings.DIFFICULTY_CHOICES, widget=CSVWidget
    )
    corrected = BooleanFilter(
        field_name="corrections", lookup_expr="isnull", exclude=True
    )

    class Meta:
        model = Post
        fields = ("language", "difficulty", "corrected")
