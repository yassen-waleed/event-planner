from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=300, blank=False)
    email = models.CharField(max_length=300, blank=False)
    relation = models.CharField(max_length=600, blank=False)

