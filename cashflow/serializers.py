from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    """Serializer for StatusModel."""
    class Meta:
        model = StatusModel
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    """Serializer for TypeModel."""
    class Meta:
        model = TypeModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for CategoryModel.
    Includes a read-only field for the type name and a foreign key to TypeModel.
    """

    type = serializers.PrimaryKeyRelatedField(queryset=TypeModel.objects.all())
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'type', 'type_name']

class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for SubCategoryModel.
    Includes a read-only field for the category name and a foreign key to CategoryModel.
    """

    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SubCategoryModel
        fields = ['id', 'name', 'category', 'category_name']

class CashFlowRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for CashFlowRecordModel.
    Includes read-only fields for status, type, category, and subcategory names.
    Also includes foreign keys to StatusModel, TypeModel, CategoryModel, and SubCategoryModel.
    """

    status_name = serializers.CharField(source='status.name', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    status = serializers.PrimaryKeyRelatedField(queryset=StatusModel.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=TypeModel.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategoryModel.objects.all())

    class Meta:
        model = CashFlowRecordModel
        fields = [
            'id', 'created_at', 'status', 'status_name',
            'type', 'type_name', 'category', 'category_name',
            'subcategory', 'subcategory_name', 'amount', 'comment'
        ]