from django.dispatch import receiver
from django.db.models.signals import post_delete
import os
from images.models import UserImages


@receiver(post_delete, sender=UserImages)
def auto_delete_file_on_delete(sender, instance: UserImages, **kwargs):
    try:
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
    except:
        pass

