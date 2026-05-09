from .models import Category, Store


def global_context(request):
    """Make categories and stores available in all templates."""
    return {
        'nav_categories': Category.objects.filter(is_active=True),
        'nav_stores': Store.objects.filter(is_active=True),
    }
