from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime


class Event(models.Model):

     event_date = models.CharField(max_length=11,default="yyyy-mm-dd")
     event_name = models.CharField(max_length=50)
     location = models.CharField(max_length=50)
     starts = models.CharField(max_length=10)
     ends = models.CharField(max_length=10)
     all_day = models.BooleanField(default=False)
     description = models.CharField(max_length=250)

     def __str__(self):
        return self.event_name

# Create your models here.
