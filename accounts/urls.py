from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import login_page,register_page , activate_email, cart, remove_cart, update_cart_item, add_review
from products.views import add_to_cart, buy_now
urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/', cart , name="cart"),
   path('buy-now/<uid>/', buy_now , name="buy-now"),
   path('add-to-cart/<uid>/', add_to_cart , name="add-to-cart"),
   path('update_cart_item/<cart_item_uid>/', update_cart_item, name='update_cart_item'),
   path('remove_cart/<cart_item_uid>/', remove_cart , name="remove_cart"),
   path('product/<uid>/add_review/', add_review, name='add_review'),
]
