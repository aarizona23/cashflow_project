from django.db import models
from django.utils import timezone

# Create your models here.

class StatusModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

class TypeModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)

class SubCategoryModel(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

class CashFlowRecordModel(models.Model):
    created_at = models.DateField(default=timezone.now)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
