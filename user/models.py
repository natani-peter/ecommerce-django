from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Trader(AbstractUser):
    phone = models.IntegerField()


class TraderImages(models.Model):
    image = models.ImageField(upload_to='user_images')
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='photos')
    profile = models.BooleanField(default=True)
