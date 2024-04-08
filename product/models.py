from django.db import models
from user.models import Trader


# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Catergory(Common):
    pass


class Attribute(models.Model):
    name = models.CharField(max_length=200)


class AttributeOption(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=200)


class SubCatergory(Common):
    attributes = models.ManyToManyField(Attribute, related_name='attributes')


class Product(Common):
    original_price = models.IntegerField()
    new_price = models.IntegerField()
    owner = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='products')
    promoted = models.BooleanField(default=False)
    posted = models.DateTimeField(auto_now=True)


class ProductImages(models.Model):
    images = models.ImageField(upload_to='product_images')
    pdt = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')
