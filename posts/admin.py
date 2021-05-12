from django.contrib import admin
from .models import Post, Correction, Translation


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    pass
