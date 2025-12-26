from django.db import models

class userData(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    branch=models.CharField(max_length=100)

