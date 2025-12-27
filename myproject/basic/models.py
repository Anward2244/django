from django.db import models
import uuid


class userData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)

class MovieBooking(models.Model):
    moviename = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    showtime = models.CharField(max_length=100)
    screenname = models.CharField(max_length=100)
    dateandtime = models.DateTimeField(auto_now_add=True)
    transaction_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

