from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Race(models.Model):
    track = models.CharField(max_length=255)
    loops = models.IntegerField
    date = models.DateTimeField


class Horse(models.Model):
    name = models.CharField(max_length=50)
    races = models.ManyToManyField(Race, through='Participation')


class Participation(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    place = models.IntegerField(null=True)


class BetType(models.Model):
    type = models.IntegerField


class Rate(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    rating = models.FloatField
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)


class Bet(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)
    bet = models.FloatField
    approved = models.BooleanField
    win = models.BooleanField
    approver = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


