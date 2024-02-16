from django.shortcuts import render, redirect   
from django.http import HttpResponse
from . models import Product, Contact, BillingQuantity, CartItem
from math import ceil
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from num2words import num2words
from datetime import datetime



# this is the logic to show the product on homepage of our shop 

def index(request):
    products= Product.objects.all()
    
    allProds=[]
    catprods= Product.objects.values('product_category', 'id')
    cats= {item["product_category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))          #no. of slides logic 
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    total_products = Product.objects.count()
    
    return render(request,'shop/index.html',params)


# this is the logic used here to show up the contact page 

def CONTACT(request):
    return render(request,'shop/contact.html')

# in contact it is used for data storing 

def contactstored(request):
    if request.method=="POST":
        print(request)
        firstname=request.POST.get('FirstName', '')
        lastname=request.POST.get('LastName', '')
        email=request.POST.get('Email', '')
        phone=request.POST.get('PhoneNumber', '')
        desc=request.POST.get('desc', '')
        contact = Contact(contact_first_name=firstname, contact_last_name= lastname ,contact_email=email, contact_phone=phone, contact_desc=desc)
        contact.save()
        messages.success(request,'Your message has been successfully received. You will be replied to soon. Thanks for contacting us 🙏. Enjoy your shopping 😊')
    return redirect('SHOPHOME')


# to show the about us page
def ABOUT(request):
    return render(request,'shop/about.html')

# search engine 
def SEARCH(request):
    return HttpResponse("SEARCH US ")

# to display the product ....
def PRODVIEW(request, myid): #here it is fetched from index page to load the product view....
    product =Product.objects.filter(id= myid)
    params = {'product': product[0]}
    return render(request, "shop/productdisplay.html",params)

# to display the product ob bill
def BILL(request, id): #here it is fetched from index page to load the product view....
    product =Product.objects.filter(id= id)
    fetchingbill = Product.objects.get(id=id)
    # number = 123
    word = num2words(fetchingbill.product_price)
    words = word.upper()
    # Get today's date
    today = datetime.today().date()

    params = {'product': product[0],
              'number_to_words' : words,
              'today_date':today}
    
    return render(request, "shop/buy.html",params)

@login_required
def MyOrders(request):
    user = request.user
    cart_items = BillingQuantity.objects.filter(user=user)
 
    total_items = sum([item.quantity for item in cart_items])

   
    context = { 
        'cart_items': cart_items,
        'total_items': total_items,
        
    }

    return render(request, 'shop/tracker.html', context)
# to add to cart the element
@login_required
def add_to_cart(request, product_id):
    user = request.user         #it is for the respective user
    product = Product.objects.get(pk=product_id)   #fteching products from database
    print(product)
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('SHOPHOME')


# to view add to cart 
@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
 
    total_items = sum([item.quantity for item in cart_items])

    total_price_per_item = {item.id: item.quantity * item.product.product_price for item in cart_items}

    # Calculate total price for all items in the cart
    total_price = sum(total_price_per_item.values())

    context = { 
        'cart_items': cart_items,
        'total_items': total_items,
        'prize_of_each': total_price_per_item,
        'total_prize': total_price,
    }

    return render(request, 'shop/view_cart.html', context)


#this is a logic to update quantity of products in cart page 
def update_quantity(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        action = request.POST.get('action')

        if action == 'increase':
            quantity += 1
        elif action == 'decrease':
            quantity -= 1
            if quantity < 1:
                quantity = 1

        try:
            cart_item = CartItem.objects.get(id=item_id)
            cart_item.quantity = quantity
            cart_item.save()
           
        except CartItem.DoesNotExist:
            messages.error(request, 'Cart item does not exist.')

    return redirect('view_cart')  # Redirect to the view_cart URL after updating quantity



#this is the logic if we want to remove the certain project from the cart 
def remove_item(request, item_id):
    # Retrieve the CartItem object using the item_id
    item = get_object_or_404(CartItem, id=item_id)
    
    # Remove the item from the cart
    item.delete()
    
    # Redirect the user back to the view cart page or any other desired page
    return redirect('view_cart')



#logic to buy  a single product 
@login_required
def buy_cart(request,bill_id):
    # return render(request,'shop/buy.html')
    user = request.user         #it is for the respective user
    product = Product.objects.get(pk=bill_id)   #fteching products from database
    print(product)
    bill_item, created = BillingQuantity.objects.get_or_create(user=user, product=product)
    if not created:
        bill_item.quantity += 1
        bill_item.save()
    messages.success(request, 'Your Order is Placed Succesfully!')
    return redirect('SHOPHOME')