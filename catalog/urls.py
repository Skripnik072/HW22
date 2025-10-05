from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView

from catalog.apps import CatalogConfig
from . import views
from catalog.views import home, contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductsCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/home/', home, name='home'),
    path('catalog/contacts/', contacts, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name = 'product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name = 'product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name = 'product_delete'),
    path('catalog/category/<int:category_id>/', ProductsCategoryView.as_view(), name = 'products_by_category'),
    ]