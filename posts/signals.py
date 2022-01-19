from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Correction


@receiver(post_save, sender=Correction)
def notification_handler(sender, instance, created, **kwargs):
    """show notification to post author when his post his corrected"""
    if created:
        instance.post.author.show_notifications = True
        instance.post.author.save()
