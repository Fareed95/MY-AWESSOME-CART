from django.contrib import admin
from .models import Product, Contact, CartItem ,BillingQuantity

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(CartItem) 
admin.site.register(BillingQuantity) 

# Register your models here.
