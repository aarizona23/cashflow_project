from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(TypeModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']

@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(CashFlowRecordModel)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']


