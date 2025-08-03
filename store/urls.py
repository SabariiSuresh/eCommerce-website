from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'), 
    path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'), 
    path('register/', views.register , name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logged_out.html'), name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-product/', views.add_product, name='add_product'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
