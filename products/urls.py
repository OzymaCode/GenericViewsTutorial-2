from django.urls import path

from .views import (
    ListProductsAPIView, 
    CreateProductAPIView
)



urlpatterns = [
    path('products/', ListProductsAPIView.as_view(), name='products-list'),
    path('products/create/', CreateProductAPIView.as_view(), name='products-list'),
]