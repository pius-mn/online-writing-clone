import imp
from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from client.models import CustomUser
# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     gender = models.CharField(max_length=50)
#     is_login = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.user.username} Profile'

class chatMessages(models.Model):
    user_from = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE,related_name="+")
    user_to = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE,related_name="+")
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
