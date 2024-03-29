from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model) :
    product_id = models.AutoField
    product_name = models.CharField(max_length =50)
    product_desc = models.CharField(max_length = 300)
    product_pub_date = models.DateField()
    product_category = models.CharField(max_length=50,default="")
    product_subcategory = models.CharField(max_length = 50, default = "")
    product_price = models.IntegerField(default=0)
    product_images = models.ImageField(upload_to="shop/images",default="")

    def __str__(self) -> str:
        return self.product_name
    
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_first_name = models.CharField(max_length = 25)
    contact_last_name = models.CharField(max_length= 25)
    contact_email = models.CharField(max_length=60)
    contact_phone = models.IntegerField(default = 0)
    contact_desc = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.contact_first_name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in {self.user.username}'s cart"

class BillingQuantity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default = None)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in {self.user.username}'s buying list"
    