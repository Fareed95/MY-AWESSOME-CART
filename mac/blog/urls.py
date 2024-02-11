from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name ="homepageofblog"),
    path("showblog/",views.showblog, name ="showblog"),
]