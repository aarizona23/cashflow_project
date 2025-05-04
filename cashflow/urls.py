from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cashflow', CashFlowViewSet, basename='cashflow')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'types', TypeViewSet, basename='type')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')

urlpatterns = [
    path('index/', index, name='index'),
    path('admin_page/', admin_view, name='admin_page'),
    path('record/', record, name='record'),
    path('api/', include(router.urls)),
]