from django import template
from pjecommerce.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    """Count number of items in cart."""
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0