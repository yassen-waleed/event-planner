from django.db import models
from users.models import User


# Create your models here.

class Rate(models.Model):
    rate = (
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'good'),
        (4, 'very good'),
        (5, 'Excellent'),
    )
    rate = models.PositiveSmallIntegerField(
        choices=rate,
        default=1,
    )




class Item(models.Model):
    name = models.CharField(max_length=300, blank=False)
    address = models.CharField(max_length=300, blank=False)
    location = models.CharField(max_length=300, blank=False)
    phone = models.TextField(blank=False)
    link = models.CharField(max_length=600, blank=False)
    about = models.CharField(max_length=1000, blank=False)
    price = models.TextField(blank=False)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    rate=models.ForeignKey(Rate,on_delete=models.CASCADE)





class customer_rating(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class type(models.Model):
    type_name = models.CharField(max_length=300, blank=False)


class items_types(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    type = models.ForeignKey(type, on_delete=models.CASCADE)


class Amenities(models.Model):
    amenities_name = models.CharField(max_length=300, blank=False)


class items_amenities(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    amenities = models.ForeignKey(Amenities, on_delete=models.CASCADE)


class availability_date(models.Model):
    availability_date = models.DateTimeField(null=False, blank=False)


class availability_Items(models.Model):
    availability_date = models.ForeignKey(availability_date, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class images(models.Model):
    item_image = models.ImageField(upload_to='images/')


class images2items(models.Model):
    image = models.ForeignKey(images,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
