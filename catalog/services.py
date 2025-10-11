from django.core.cache import cache
from catalog.models import Product, Category
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    '''Получает из кэша информацию о продуктах, если кэш пуст - получает из БД'''
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

class ProductsService:

    @staticmethod
    def get_products_by_category(category):
        # Получаем имя выбранной категории
        name_category = Category.objects.get(id=category)
        print("Names categories:", name_category)  # Отладочный вывод
        # Получаем список продуктов в выбранной категории
        products = Product.objects.filter(categor=name_category)
        print("Names products:", products)  # Отладочный вывод
        return products