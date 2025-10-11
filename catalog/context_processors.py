from catalog.models import Category


def categories_processor(request):
    return {'list_category': Category.objects.all()}
