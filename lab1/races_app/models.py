from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Horse(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Race(models.Model):
    track = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    loops = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.track


class BetType(models.Model):
    type = models.IntegerField()


class Participation(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='participants')
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    place = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.horse.name


class Bet(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    participant = models.ForeignKey(Participation, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(default=0)
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)
    bet = models.FloatField(default=0)
    approved = models.BooleanField()
    win = models.BooleanField()
    approver = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255)
