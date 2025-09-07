from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'categor')
    list_filter = ('categor',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

