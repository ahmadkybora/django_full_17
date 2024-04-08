from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializers

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializers = ArticleSerializers(articles, many=True, context={ "request": request })
    return Response(serializers.data, status=status.HTTP_200_OK)
