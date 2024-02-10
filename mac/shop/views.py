from django.shortcuts import render, redirect   
from django.http import HttpResponse
from . models import Product, Contact
from math import ceil
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required


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
    total_products = Product.objects.count()
    print(f'Total Number of Products: {total_products}')
    # params = {"product":products,"no_of_slides":nSlides, "range": range(1,nSlides)}
    return render(request,'shop/index.html',params)


def CONTACT(request):
    return render(request,'shop/contact.html')

def contactstored(request):
    if request.method=="POST":
        print(request)
        firstname=request.POST.get('FirstName', '')
        lastname=request.POST.get('LastName', '')
        email=request.POST.get('Email', '')
        phone=request.POST.get('PhoneNumber', '')
        desc=request.POST.get('desc', '')
        # print(firstname,lastname,email,phone, desc )
        contact = Contact(contact_first_name=firstname, contact_last_name= lastname ,contact_email=email, contact_phone=phone, contact_desc=desc)
        contact.save()
    return render(request,'shop/contactstored.html')



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


@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('SHOPHOME')

@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
 
    total_items = sum([item.quantity for item in cart_items])
    total_price= sum([item.quantity * item.product.product_price for item in cart_items])
    total_price_of_resp = [item.quantity * item.product.product_price for item in cart_items]

    context = { 
        'cart_items': cart_items,
        'total_items': total_items,
        'prize_of_each': total_price_of_resp,
        'total_prize': total_price,
    }

    return render(request, 'shop/view_cart.html', context)