from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil
# Create your views here.
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('product_category', 'id')
    cats= {item["product_category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    
    # params = {"product":products,"no_of_slides":nSlides, "range": range(1,nSlides)}
    return render(request,'shop/index.html',params)


def CONTACT(request):
    return HttpResponse("CONTACT US ")


def ABOUT(request):
    return render(request,'shop/about.html')


def SEARCH(request):
    return HttpResponse("SEARCH US ")


def PRODVIEW(request, myid):
    # fetching proiducts
    product =Product.objects.filter(id= myid)
    
    return render(request, "shop/productdisplay.html",{'product': product[0]})



def CART(request):
    return HttpResponse("CART")


