from django.urls import path
from public import views

urlpatterns = [
    path('api/slug/<slug:slug>/',view=views.RestaurantDetailView.as_view(), kwargs={'lookup_field':'slug'}),
    # path('api/id/<int:pk>/', view=views.RestaurantDetailView.as_view())
]