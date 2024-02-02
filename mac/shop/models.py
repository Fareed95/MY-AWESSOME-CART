from django.db import models

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