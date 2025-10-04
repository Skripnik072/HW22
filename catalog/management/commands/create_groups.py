from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='moderator')
        permissions = Permission.objects.filter(codename__in=['can_unpublish_product', 'can_delete_product'])
        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана с необходимыми правами.'))