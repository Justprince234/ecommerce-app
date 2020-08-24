from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.core.paginator import Paginator
from pjecommerce.models import Item, OrderItem, Order
# Create your views here.
def home(request):
    """Renders the home page.""""
    items = Item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    template_name = 'pjecommerce/home.html'
    content = {
        'items': items,
        'pages': pages,
    }

    return render(request, template_name, content)

def products(request, slug):
    """Renders product page."""
    items = get_object_or_404(Item, slug=slug)
    template_name = 'pjecommerce/product.html'
    content = {
        'items': items
    }

    return render(request, template_name, content)

def add_to_cart(request, slug):
    """Add item to cart."""
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False 
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Item added to cart successfully.')
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect('pjecommerce:product', slug=slug)

def remove_from_cart(request, slug):
    """Remove item from cart."""
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False 
            )[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was successfully removed from cart.')
            return redirect('pjecommerce:product', slug=slug)
        else:
            messages.info(request, 'Item not in cart.')
            return redirect('pjecommerce:product', slug=slug)
    else:
        messages.info(request, 'You do not have an an active order.')
        return redirect('pjecommerce:product', slug=slug) 
    return redirect('pjecommerce:product', slug=slug)


def checkout(request):
    template_name = 'pjecommerce/checkout.html'

    return render(request, template_name)

def contact(request):
    template_name = 'pjecommerce/contact.html'

    return render(request, template_name)