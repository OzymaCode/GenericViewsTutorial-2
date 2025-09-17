from django.urls import path

from .views import (
    ListProductsAPIView, 
    CreateProductAPIView,
    RetrieveProductAPIView,
    UpdateProductAPIView,
    DestroyProductAPIView
)



urlpatterns = [
    path('products/', ListProductsAPIView.as_view(), name='products-list'),
    path('products/create/', CreateProductAPIView.as_view(), name='products-list'),
    path('products/retrieve/<slug:slug>/', RetrieveProductAPIView.as_view(), name='products-retrieve'),
    path('products/update/<slug:slug>/', UpdateProductAPIView.as_view(), name='products-update'),
    path('products/destroy/<slug:slug>/', DestroyProductAPIView.as_view(), name='products-destroy'),
]