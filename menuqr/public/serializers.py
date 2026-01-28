from rest_framework.serializers import ModelSerializer
from restaurants.models import Restaurants
from menu.models import MenuCategory, MenuItem
class MenuItemSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MenuItem
class MenuCategorySerializer(ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        fields = "__all__"
        model = MenuCategory

class RestaurantSerializer(ModelSerializer):
    menu_categoties = MenuCategorySerializer(many=True, read_only=True)
    class Meta:
        fields = "__all__"
        model = Restaurants