from django.db import models
from guests.models import Guest
from items.models import Item
# Create your models here.
from users.models import User


class event (models.Model):
    name = models.CharField(max_length=600, blank=False)
    type = models.CharField(max_length=600, blank=False)
    location = models.CharField(max_length=600, blank=False)
    Date = models.DateField(blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class event_Guests(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete=models.CASCADE)

class events_items(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    items = models.ForeignKey(Item ,on_delete=models.CASCADE)

class event_schdual(models.Model):
    action = models.TextField(blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event = models.ForeignKey(event, on_delete=models.CASCADE)


