from django.urls import path

from .views import (
    ListCreateProductsAPIView, 
    RetrieveUpdateDestroyProductAPIView,
)



urlpatterns = [
    path('products/', ListCreateProductsAPIView.as_view(), name='products-list'),
    path('products/<slug:slug>/', RetrieveUpdateDestroyProductAPIView.as_view(), name='products-retrieve'),
]