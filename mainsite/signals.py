from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cat, Student


@receiver(post_save, sender=Cat)
def update_number_of_cats(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        student.number_of_cats += 1
        student.save()
