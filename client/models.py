from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    country = models.CharField(null = True,blank = True,default = "Kenya",max_length=100)
    about = models.CharField(null=True, blank=True,max_length=1000)
    ratings = models.IntegerField(null=True, blank=True)
    is_specialVerified = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True, default='user-avatar-placeholder.png')
    otp = models.IntegerField(null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    amount_spent = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['username', 'phone', ]
    USERNAME_FIELD = 'email'
    def __str__(self):
        return f'{self.username} Profile'

    def get_username(self):
        return self.username

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def ban_user(self):
        self.is_active = False
        self.save()

    def unban_user(self):
        self.is_active = True
        self.save()


class Jobs(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    jobId = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    delivery_qty = models.IntegerField(blank=True, null=True)
    delivery_type = models.CharField(max_length=200, blank=True, null=True)
    min_salary = models.CharField(max_length=200,blank=True,null=True)
    max_salary = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null= True)
    uploadedfile = models.FileField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_regected = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.jobId
    # def save(self, *args, **kwargs):
    #     if self.due_date is None:
    #         self.due_date = self.created_at +  datetime.timedelta(days=self.delivery_qty)
    #     super(Jobs, self).save(*args,**kwargs)

class Bids(models.Model):
    username= models.CharField(max_length=100, blank=True, null=True)
    jobId= models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)
    workingDays = models.CharField(blank=True, null=True,max_length=100)

    # def __str__(self):
    #     return self.username


class Funds(models.Model):
    amount = models.CharField(blank=True, null=True,max_length=200)
    reciver = models.CharField(blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    transaction_id = models.CharField(blank=True,null=True, max_length=200)
    payment_method = models.CharField(blank=True, null=True, max_length=100)
    status = models.CharField(default='unpaid', max_length=100)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    jobId = models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.transaction_id

