from django.db import models
from user.models import Trader
from product.models import Product


# Create your models here.

class Review(models.Model):
    owner = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='writer')
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='written_about')
    content = models.TextField()


class Rating(models.Model):
    rate = models.IntegerField()
    rated_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')