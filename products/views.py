from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from accounts.models import Cart, CartItems,Review
from django.contrib.auth.decorators import login_required

@login_required
def get_product(request , uid):
    try:
        product = Product.objects.get(uid =uid)
        reviews = Review.objects.filter(product=product)
        print(reviews)
        for review in reviews:
            print(f'Review by {review.user_profile.user.username}: {review.review} on {review.created_at}')
        quantity_options = range(1, 11)
        context = {'product': product, 'quantity_options': quantity_options, 'reviews':reviews}

        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)

@login_required  
def add_to_cart(request, uid):
    quantity = request.GET.get('quantity', 1)
    product = Product.objects.get(uid=uid)  # Assuming Product model has a uid field
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    # Check if the product is already in the cart
    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

    if not created:
        # If the item is already in the cart, update the quantity
        cart_item.quantity = int(cart_item.quantity) + int(quantity)
        cart_item.save()
    else:
        # If the item is not in the cart, create a new cart item
        cart_item.quantity = quantity
        cart_item.save()

    # Redirect to the product detail page or any other desired page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def buy_now(request, uid):
    quantity = request.GET.get('quantity', 1)
    product = Product.objects.get(uid=uid)  # Assuming Product model has a uid field
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    # Check if the product is already in the cart
    cart_item = CartItems.objects.create(cart=cart,product=product, quantity=quantity)
    cart_item.save()

    # Redirect to the product detail page or any other desired page
    return redirect('cart')