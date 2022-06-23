from datetime import datetime

from django.db import models

from event_planner import settings
from Items.models import Item
# Create your models here.
from users.models import User


class event(models.Model):
    name = models.CharField(max_length=600, blank=False)
    type = models.CharField(max_length=600, blank=False)
    location = models.CharField(max_length=600, blank=False)
    Date = models.DateTimeField(blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)


class event_schdual(models.Model):
    action = models.TextField(blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event = models.ForeignKey(event, on_delete=models.CASCADE)
