from django.db import models

# from django.contrib.auth.models import User
# from djongo import models
from datetime import date


class Rhymes(models.Model):
    user = models.CharField(max_length=250)
    word = models.CharField(max_length=250)
    date = models.CharField(max_length=250, default=date.today())
    word_of_the_day = models.CharField(max_length=250, default="")
    is_accepted = models.BooleanField(default=False)
    


class WordOfTheDay(models.Model):
    date = models.CharField(max_length=250)
    Word_of_the_day = models.CharField(max_length=250, default="")

class Accepted(models.Model):
    user = models.CharField(max_length=250)
    word = models.CharField(max_length=250)
    date = models.CharField(max_length=250, default=date.today())
    Word_of_the_day = models.CharField(max_length=250, default="")
    is_accepted = models.BooleanField(default=True)
    count = models.IntegerField(default=0)

class Rejected(models.Model):
    user = models.CharField(max_length=250)
    word = models.CharField(max_length=250)
    date = models.CharField(max_length=250, default=date.today())
    Word_of_the_day = models.CharField(max_length=250, default="")
    is_accepted = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    

