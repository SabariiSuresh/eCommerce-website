from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .cart import Cart
from .forms import OrderForm
from .forms import ProductForm
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    categories = Product.CATEGORY_CHOICE        

    return render( request , 'store/home.html' , {'products' : products , 'query' : query , 'category' : category , 'categories' : categories })

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request , 'store/add_product.html' , {'form' : form}) 


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/profile.html', {'orders': orders})


def add_to_cart( request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.add(product)
    return redirect('cart_detail')


def remove_from_cart(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request , 'store/cart.html', {'cart' : cart})


def increase_quantity(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.increase(product)
    return redirect('cart_detail')


def decrease_quantity(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.decrease(product)
    return redirect('cart_detail')    


def product_detail(request , product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request , 'store/product_detail.html' , { 'product' : product})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
       form = UserCreationForm()
    return render(request , 'store/register.html' , {'form' : form})           


@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()

            cart.clear()

            return render(request, 'store/order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {'cart': cart, 'form': form})    




