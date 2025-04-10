from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == 'marketplace':  # Only run for this app
        default_categories = ["Architecture", "Engineering", "Pharmacy"]
        for name in default_categories:
            Category.objects.get_or_create(name=name)
