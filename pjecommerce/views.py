from django.shortcuts import render
from pjecommerce.models import Item

# Create your views here.
def home(request):
    template_name = 'pjecommerce/home.html'
    content = {
        'items': Item.objects.all()
    }

    return render(request, template_name, content)

def products(request):
    template_name = 'pjecommerce/products.html'

    return render(request, template_name)

def checkout(request):
    template_name = 'pjecommerce/checkout.html'

    return render(request, template_name)

def contact(request):
    template_name = 'pjecommerce/contact.html'

    return render(request, template_name)