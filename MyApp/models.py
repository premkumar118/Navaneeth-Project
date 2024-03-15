from django.db import models

# Create your models here.

class Register(models.Model):
        Name = models.CharField(max_length = 50, default="")
        Mail = models.CharField(max_length = 50, default="")
        Number = models.CharField(max_length = 50, default="")
        Password = models.CharField(max_length = 50, default="")
        Address = models.CharField(max_length = 50, default="")
        PinCode = models.CharField(max_length = 50, default="")

class Booking(models.Model):
        Name = models.CharField(max_length = 50, default="")
        Booking = models.CharField(max_length = 50, default="")
        Number = models.CharField(max_length = 50, default="")
        Date = models.CharField(max_length = 50, default="")
        BookingNumber = models.CharField(max_length = 50, default="")