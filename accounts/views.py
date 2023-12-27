from cmath import log
from tkinter import E
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Cart, CartItems, Profile


def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    

def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid = cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_cart_item(request, cart_item_uid):
    # Assuming you receive the new quantity from a form
    print(request.POST)
    new_quantity = request.POST.get('quantity')

    # Retrieve the cart item
    try:
        cart_item = CartItems.objects.get(uid = cart_item_uid)

        # Update the quantity if a valid new quantity is provided
        if new_quantity and new_quantity.isdigit():
            cart_item.quantity = int(new_quantity)
            cart_item.save()
    except Exception as e:
        print(e)

    # Redirect back to the cart page or wherever is appropriate
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):
    cart_items = CartItems.objects.all()
    quantity_options = range(1, 11)

    for item in cart_items:
        product_name = item.product.product_name if item.product else None
        product_images = item.product.product_images.all() if item.product else None

        print(f"Product Name: {product_name}, Quantity: {item.quantity}")

        for image in product_images:
            print(f"Image: {image.image.url}")

    total = cart_items[0].cart.get_cart_total() if cart_items else None

    # Note: Adjust this part based on how you want to handle the total
    total_value = total if total is not None else 0

    context = {'cart': cart_items, 'total': total_value, 'quantity_options': quantity_options}
    return render(request, 'accounts/cart.html', context)

