from django.db import models
from accounts.models import RestaurantOwner
# Create your models here.

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    owner_id = models.ForeignKey(RestaurantOwner,on_delete=models.CASCADE)