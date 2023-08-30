from catalog.serializers.admin import (
    CreateCategorySerializer,
    CategoryTreeSerializer,
    CategoryNodeSerializer,
    CategoryUpdateSerializer,
    )
from catalog.models import Category
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    
    # queryset = Category.objects.all()
    # serializer_class = CreateCategorySerializer
    def get_queryset(self):
        if self.action == "list":
            return Category.objects.filter(depth=1) #depth=1 only show the first branch of trees and their children
        else :
            return Category.objects.all()
    def get_serializer_class(self):
        match self.action: #python:3:10+
            case "list" : 
                return CategoryTreeSerializer
            case "create" : 
                return CreateCategorySerializer
            case "retrieve":
                return CategoryNodeSerializer
            case "update":                      #put (we must write all required fields for updating)
                return CategoryUpdateSerializer
            case "partial_update":              #patch 
                return CategoryUpdateSerializer
            case "destroy":                     #delete 
                return CategoryUpdateSerializer #No matter what is the view
            case _:
                raise "this is finally"

        # if self.action == "list":
        #     return CategoryTreeSerializer
        # elif self.action == "create":
        #     return CreateCategorySerializer
    