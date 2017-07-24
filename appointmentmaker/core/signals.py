from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from core.models import Appointee


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    """Create a User object for every Django User."""
    if created:
        Appointee.objects.get_or_create(user=instance)
