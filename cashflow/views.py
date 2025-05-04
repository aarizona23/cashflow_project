from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFromToRangeFilter
from .models import *
from .serializers import (
    StatusSerializer, TypeSerializer, CategorySerializer,
    SubCategorySerializer, CashFlowRecordSerializer
)
import django_filters
from django.shortcuts import render

def record(request):
    """Renders the record page."""
    return render(request, 'cashflow/record.html')

def index(request):
    """Renders the index page."""
    return render(request, 'cashflow/index.html')

def admin_view(request):
    """Renders the admin page with entities."""
    entities = {
        'statuses': 'Статусы',
        'types': 'Типы',
        'categories': 'Категории',
        'subcategories': 'Подкатегории'
    }
    return render(request, 'cashflow/admin.html', {'entities': entities})

class CashFlowFilter(FilterSet):
    """
    FilterSet for filtering CashFlow records.
    Allows filtering by created_at date range, status, type, category, and subcategory.
    """

    created_at = DateFromToRangeFilter()
    status = django_filters.NumberFilter(field_name='status__id')
    type = django_filters.NumberFilter(field_name='type__id')
    category = django_filters.NumberFilter(field_name='category__id')
    subcategory = django_filters.NumberFilter(field_name='subcategory__id')

    class Meta:
        model = CashFlowRecordModel
        fields = ['created_at', 'status', 'type', 'category', 'subcategory']

class CashFlowViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing CashFlow records.
    Provides CRUD operations and filtering capabilities.
    """

    queryset = CashFlowRecordModel.objects.select_related(
        'status', 'type', 'category', 'subcategory'
    ).all()
    serializer_class = CashFlowRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CashFlowFilter
    ordering_fields = ['created_at', 'amount']
    ordering = ['-created_at']

class StatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Status records.
    Provides CRUD operations for status entities.
    """

    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer

class TypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Type records.
    Provides CRUD operations for type entities.
    """

    queryset = TypeModel.objects.all()
    serializer_class = TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Category records.
    Provides CRUD operations for category entities.
    Allows filtering by type.
    """

    queryset = CategoryModel.objects.select_related('type').all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        type_id = self.request.query_params.get('type')
        if type_id:
            queryset = queryset.filter(type_id=type_id)
        return queryset

class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing SubCategory records.
    Provides CRUD operations for subcategory entities.
    Allows filtering by category.
    """
    
    queryset = SubCategoryModel.objects.select_related('category').all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


