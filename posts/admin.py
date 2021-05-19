from django.contrib import admin
from .models import Post, Correction, Text


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    pass
