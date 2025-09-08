from django.core.management.base import BaseCommand
from catalog.models import Product, Category

'''Реализация кастомной команды для заполнения БД'''
class Command(BaseCommand):
    help = 'Добавление продуктов в БД'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name="Грибы", description='Съедобные')

        products = [
            {'name': 'Грузди', 'description': 'Желтые', 'price': 200, 'created_at': '2025-09-06', 'updated_at': '2025-09-06',
             'categor': category},
            {'name': 'Грузди', 'description': 'Белые', 'price': 210, 'created_at': '2025-09-06', 'updated_at': '2025-09-06',
             'categor': category},
            ]

        for prod in products:
            products, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Продукт успешно добавлен в БД: {products.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Продукт уже существует в БД: {products.name}'))