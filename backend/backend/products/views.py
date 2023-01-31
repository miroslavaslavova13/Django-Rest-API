from rest_framework.generics import RetrieveAPIView

from backend.products.models import Product
from backend.products.serializers import ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

