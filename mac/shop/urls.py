from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="SHOPHOME"),
    path("CONTACT",views.CONTACT, name="CONTACT"),
    path("ABOUT",views.ABOUT, name="ABOUT"),
    path("SEARCH",views.SEARCH, name="SEARCH"),
    path("products/<int:myid>",views.PRODVIEW, name="PRODVIEW"),
    path("CART",views.CART, name="CART"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)