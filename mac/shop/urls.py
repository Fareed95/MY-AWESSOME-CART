from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="SHOPHOME"),
    path("CONTACT",views.CONTACT, name="CONTACT"),
    path("contactstored",views.contactstored, name="CONTACTSDTORED"),
    path("ABOUT",views.ABOUT, name="ABOUT"),
    path("SEARCH",views.SEARCH, name="SEARCH"),
    path("products/<int:myid>",views.PRODVIEW, name="PRODVIEW"),
    path("CART",views.CART, name="CART"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)