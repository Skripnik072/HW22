from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.set_password("Viktor")
        user.is_active = True
        user.is_staff = True
        User.is_superuser = True
        user.save()
