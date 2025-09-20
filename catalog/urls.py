from django.urls import path, include
from django.views.generic import DetailView

from catalog.apps import CatalogConfig
from . import views
from catalog.views import home, contacts, ProductListView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/home/', home, name='home'),
    path('catalog/contacts/', contacts, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name = 'product_create')
    ]