from django.urls import path
from pjecommerce import views

app_name = 'pjecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.products, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
]