from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
    return Response(serializer.data)
