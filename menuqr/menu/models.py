from django.db import models
from restaurants.models import Restaurants
# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    restaurant_id = models.ForeignKey(Restaurants,on_delete=models.CASCADE)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category_id = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)