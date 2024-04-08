from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from products.models import Product
from categories.models import Category

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializeres = ProductSerializer(products, many=True, context={ "request": request })
    return Response(serializeres.data, status=status.HTTP_200_OK)
