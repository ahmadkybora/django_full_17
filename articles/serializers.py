from rest_framework import serializers
from .models import Article

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image']
