from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Product
from .serializers import ProductSerializer

class ListProductsAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
