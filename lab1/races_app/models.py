from django.db import models

# Create your models here.


class Horse(models.Model):
    name = models.CharField(max_length=50)
    races = models.ManyToManyField(Race, through='Participation')


class Participation(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    place = models.IntegerField(null=True)


class Race(models.Model):
    track = models.CharField(max_length=255)
    loops = models.IntegerField
    date = models.DateTimeField


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)


class Client(User):
    phone = models.CharField(max_length=15)


class Administrator(User):
    nickname = models.CharField(max_length=127)


class Bookmaker(User):
    rating = models.FloatField


class Rate(models.Model):
    creator = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    rating = models.FloatField
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)


class BetType(models.Model):
    type = models.IntegerField


class Bet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)
    bet = models.FloatField
    approved = models.BooleanField
    win = models.BooleanField
    approver = models.ForeignKey(Administrator, on_delete=models.CASCADE, null=True)


