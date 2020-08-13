from django.db import models
from django.urls import reverse
from  django.conf import settings

# Create your models here.
CATERGORY_CHOICES = (
    ('S', 'Shirts'),
    ('SW', 'Sport Wears'),
    ('OW', 'Outwears'),
)

LABEL_CHOICES = (
    ('P', 'pimary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

class Item(models.Model):
    """Creates a database instance Item in database."""
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=CATERGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse('pjecommerce:add-to-cart', kwargs={'slug':self.slug})



class OrderItem(models.Model):
    """Creates a database instance OrderItem in database."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    """Creates a database instance Order in database."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user}"

