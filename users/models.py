from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_vendor=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)

    def __str__(self) :
        return self.username
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Manager(models.Model):
    user = models.OneToOneField(User,related_name='admin',on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Customer(models.Model):
    user=models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    phone=models.CharField(max_length=12, null=True, blank=True)
    bank_name=models.CharField(max_length=100, null=True, blank=True)
    bank_number=models.TextField(null=True, blank=True)
    account_type=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username



class Vendor(models.Model):
    user=models.OneToOneField(User, related_name="vendor", on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=12, null=True, blank=True)
    bank_name=models.CharField(max_length=100, null=True, blank=True)
    bank_number=models.TextField(null=True, blank=True)
    account_type=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.company_name