from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from restaurants.models import Restaurants
from public.serializers import RestaurantSerializer
from menu.models import MenuCategory, MenuItem
from rest_framework.generics import RetrieveAPIView
# Create your views here.
def test(request):
    return HttpResponse("OK!")

# class MenuView(APIView):
#     def get_restaurant(self,slug):
#         try:
#             restaurant = Restaurants.objects.get(slug=slug)
#             return restaurant
#         except:
#             raise Http404
        
#     def get(self, request, slug):
#         restaurant = self.get_restaurant(slug=slug)
#         serializer = RestaurantSerializer(restaurant)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'slug'


