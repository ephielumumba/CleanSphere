from django.db import models

# Create your models here.
class User(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    position=models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Donate(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    email = models.EmailField()
    amount = models.IntegerField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class WaterData(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    waterbody = models.CharField(max_length=100)
    water_colour = models.CharField(max_length=100)
    smell = models.CharField(max_length=100)
    odor_description = models.CharField(max_length=100)
    pollution_evidence = models.CharField(max_length=100)  # Stores multiple choices as a comma-separated string
    turbidity = models.FloatField()
    ph = models.FloatField()
    nitrates = models.FloatField()
    phosphates = models.FloatField()
    oxygen = models.FloatField()
    algae_blooms = models.CharField(max_length=100)
    aquatic_life = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


