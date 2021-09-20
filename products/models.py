from django.db import models


# Create your models here.
              #module.class
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    #this line is used to upload all the images in products page
    image_url = models.ImageField(upload_to='Images/')  # since url are of 2083 max characters
    @staticmethod
    #by unique id the products are loading into the page
    #method to get by id
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)


class Offer(models.Model):
    #for coupen code 
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()