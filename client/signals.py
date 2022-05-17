from django.db.models.signals import post_save
from .mails import otp_email
from .models import CustomUser
import random


def registered(sender, instance, created, **kwargs):
    if created:
        user = instance
        otp = user.otp
        otp_email(otp, user.username, user.email)


post_save.connect(registered, sender=CustomUser)
