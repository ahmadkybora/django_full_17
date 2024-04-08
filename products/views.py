from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True, context={ "request": request })
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, context={ "request": request })
    return Response(serializer.data, status=status.HTTP_200_ok)
