from django.db import models
from  django.conf import settings

# Create your models here.
class Item(models.Model):
    """Creates a database instance Item in database."""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    """Creates a database instance OrderItem in database."""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    """Creates a database instance Order in database."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField()
    ordered_date = models.DateTimeField()
    oredered = models.BooleanField(default=False)


    def __str__(self):
        return self.title

