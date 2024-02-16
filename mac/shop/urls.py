from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="SHOPHOME"),#it fetch the shop main page 

    path("CONTACT",views.CONTACT, name="CONTACT"), #it fetch the contact page 

    path("contactstored",views.contactstored, name="CONTACTSDTORED"),  #it fetch the contact page but after submimitting details 

    path("ABOUT",views.ABOUT, name="ABOUT"), #it fetch the about page 

    path("SEARCH",views.SEARCH, name="SEARCH"), #it fetch the search page {working on it is pending}

    path("products/<int:myid>",views.PRODVIEW, name="PRODVIEW"), #it fetch the id of the product where it is touched and used to send in the productdispay page 

    path("billproduct/<int:id>",views.BILL, name="BILL"), #it fetch the id of the product where it is touched and used to send in the bill page 

    path('TRACKER',views.MyOrders, name = "MyOrders"),#it fetch the tracker page 

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), #it is used to store the respective product in add to cart in add to cart page it is taken from index as well as from product dispay page \

    path('buy_cart/<int:bill_id>/', views.buy_cart, name='buy_cart'), #it is used to load the buy element means if anyone wishes to buy the product then it is used 

    path('view_cart/', views.view_cart, name='view_cart'), #it is used to view the cart element 

    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'), #it is used to increase or decrease the quantity of a product in add to cart page 
    
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'), # it is used to remove any element if anyone wishes to remove it from the add to caert 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)