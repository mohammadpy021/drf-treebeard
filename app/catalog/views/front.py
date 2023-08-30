from catalog.serializers.front import CategorySerializer
from catalog.models import Category
from rest_framework import viewsets

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Category.objects.public()
    serializer_class = CategorySerializer
