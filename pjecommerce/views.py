from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from  django.conf import settings
from pjecommerce.models import Item, OrderItem, Order
# Create your views here.
def home(request):
    items = Item.objects.all()
    template_name = 'pjecommerce/home.html'
    content = {
        'items': items
    }

    return render(request, template_name, content)

def products(request, slug):
    items = get_object_or_404(Item, slug=slug)
    template_name = 'pjecommerce/product.html'
    content = {
        'items': items
    }

    return render(request, template_name, content)

def add_to_cart(request, slug):
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
        messages.info(request, 'This item was successfully added to cart.')
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect('pjecommerce:product', slug=slug)

def remove_from_cart(request, slug):
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
        else:
            messages.info(request, 'This item was not in your cart.')
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