from django.urls import path
from . import views

app_name = 'pjecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]