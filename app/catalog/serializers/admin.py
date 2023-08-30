from rest_framework import serializers
from catalog.models import Category
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_field
# from django.core.serializers import serialize
# import json

class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    # @extend_schema_field(serializers.ListField)
    def get_children(self, obj) :
        return CategoryTreeSerializer(obj.get_children(), many=True).data   #this way is more complete
        # return json.loads(serialize("json",obj.get_children())) 

    class Meta:
        model = Category
        fields = ["id", "title", "description","is_public", "slug", "children"] 
CategoryTreeSerializer.get_children = extend_schema_field(serializers.ListField(child=CategoryTreeSerializer())) (CategoryTreeSerializer.get_children)#the last (CategoryTreeSerializer.get_children) is exactly like the code after @... and we do this because we need to assign the class to the function (recursive)

class CreateCategorySerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        parent = validated_data.pop('parent', None)
        if(parent is None):
            instance = Category.add_root(**validated_data)
        else: 
            parent_node = get_object_or_404(Category, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance
        # return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    class Meta:
        model = Category
        fields = ["id", "title", "description","is_public", "slug", "parent"]

class CategoryNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "description","is_public",]

