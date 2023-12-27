from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from products.models import Product, SizeVariant
from accounts.models import Cart, CartItems




def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        context = {'product': product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            print(price)

        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)

def add_to_cart(request, slug):
    varient = request.GET.get('varient')
    
        
    product = Product.objects.get(slug =slug)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user = user, is_paid = False)
    
    cart_item = CartItems.objects.create(cart = cart, product = product,)
    
    if varient:
        varient = request.GET.get(varient)
        size_varient = SizeVariant.objects.get(size_name = varient)
        cart_item.size_varient = size_varient
        cart_item.save()

    return HttpResponseRedirect(request.path_info)