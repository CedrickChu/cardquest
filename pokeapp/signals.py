from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
import os
from .models import Trainer

@receiver(post_save, sender=Trainer)
def copy_trainer_image(sender, instance, **kwargs):
    if instance.image:
        source_path = instance.image.path
        target_path = os.path.join('pokeapp', 'static', 'images', f'{instance.name.lower()}.png')

        with open(source_path, 'rb') as source_file:
            with open(target_path, 'wb') as target_file:
                target_file.write(source_file.read())
