from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order, dispatch_uid="send_email")
def send_email(sender, instance, **kwargs):
    print('ok')