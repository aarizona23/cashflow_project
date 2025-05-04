from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=TypeModel.objects.all())
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'type', 'type_name']

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SubCategoryModel
        fields = ['id', 'name', 'category', 'category_name']

class CashFlowRecordSerializer(serializers.ModelSerializer):
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