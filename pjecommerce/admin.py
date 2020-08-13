from django.contrib import admin
from pjecommerce.models import Item, OrderItem, Order

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)