from django.urls import path

from.views import ListProductsAPIView




urlpatterns = [
    path('products/', ListProductsAPIView.as_view(), name='products'),
]