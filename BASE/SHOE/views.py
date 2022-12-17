from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.http import JsonResponse
import json
from django.views import View

# Create your views here.
# Home page
def home(request):
    current_user=request.user
    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=current_user)
    # print(current_user, ":", current_user.id)
    return render(request, 'home.html')

# Shoe function to filter shoes by gender and type
def shoes(request, gender, type=None):
    shoes = Shoe.objects.filter(gender=gender, type=type)
    return render(request, 'shoes.html',{'shoes':shoes})

# Men's shoes
def shoes_mens(request):
    shoes_mens=Shoe.objects.filter(gender='1')
    return render(request, 'shoes.html', {'shoes':shoes_mens})

def shoes_mens_athl(request):
    return shoes(request, gender='1',type='1')

def shoes_mens_drss(request):
    return shoes(request, gender='1',type='2')

def shoes_mens_work(request):
    return shoes(request, gender='1',type='3')

def shoes_mens_casl(request):
    return shoes(request, gender='1',type='4')

# Women's shoes
def shoes_womens(request):
    shoes_womens=Shoe.objects.filter(gender='2')
    return render(request, 'shoes.html', {'shoes':shoes_womens})

def shoes_womens_athl(request):
    return shoes(request, gender='2',type='1')

def shoes_womens_drss(request):
    return shoes(request, gender='2',type='2')

def shoes_womens_work(request):
    return shoes(request, gender='2',type='3')

def shoes_womens_casl(request):
    return shoes(request, gender='2',type='4')

# Signup
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(User.username)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

"""The following cart views work with the javascript functions found in static/js/cart.js in order to allow the user to add, remove, and change the quantity of shoes in their cart"""
# Cart
@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
        return redirect('login')

    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})

# Update cart
@login_required
def updateCart(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        shoeId = data["shoeId"]
        action = data["action"]
        shoe = Shoe.objects.get(id=shoeId)
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitem, created = CartItems.objects.get_or_create(cart = cart, shoe = shoe)
        if action == "add":
            cartitem.quantity += 1
            cartitem.save()
        if action == "clear":
            cartitem.quantity=0
            cartitem.save()
    else:
        return redirect('login')

    return JsonResponse("Cart Updated", safe = False)

# Update quantity in cart
@login_required
def updateQuantity(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        quantityFieldValue = data['qfv']
        quantityFieldShoe = data['qfp']
        shoe = CartItems.objects.filter(shoe__name = quantityFieldShoe).last()
        shoe.quantity = quantityFieldValue
        shoe.save()
        return JsonResponse("Quantity updated", safe = False)

# Clear cart
@login_required
def clearCart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart = Cart.objects.filter(customer = customer, completed = False)
        cart.delete()
        return redirect('cart')

# Search bar functionality
class SearchView(View):
    def get(self, request):
        query = request.GET.get("query")
        shoes = Shoe.objects.filter(name__contains=query) | Shoe.objects.filter(brand__contains=query)
        return render(request, 'shoes.html', {'shoes':shoes})