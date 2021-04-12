from datetime import datetime, date, time

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http.response import HttpResponseForbidden
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

# Add a item to the cart
from ..models import Item
from ..models.order import Cart_line, Cart, Order


@login_required(login_url="login")
def add_to_cart(request, item_id):
    if request.POST['quantity'] == "0":
        return render(request, "ubs_project/merchandise/error.html", {"message": "quantity muse be > 0"}, status=400)
    else:
        quantity = int(request.POST['quantity'])
    # Try to retrieve an existing cart
    try:
        cart = Cart.objects.filter(user=request.user).get(is_ordered=False)
    # If it doesn't exist, create one for the user
    except Cart.DoesNotExist:
        cart = Cart(user=request.user)
        cart.save()

    # Get the selected item and add to cart
    item = Item.objects.get(id=item_id)
    cart.add(item, quantity)
    return redirect("cart")


# Delete a line of the cart
@login_required(login_url="login")
def delete_from_cart(request, cart_line_id):
    try:
        Cart_line.objects.get(id=cart_line_id).delete()
    except ObjectDoesNotExist:
        return render(request, "merchandise/error.html",
                      {"message": "could not delete the Pizza : Pizza does not exist"},
                      status=404)
    return redirect("cart")


# Allows a user to order the selection in the cart
@login_required(login_url="login")
def order_cart(request):
    # Get the actuel non-ordered yet cart of the user
    cart = Cart.objects.filter(user=request.user).get(is_ordered=False)
    # Create an order with that cart
    order = Order(cart=cart)
    # Set that particular cart to "ordered"
    cart.is_ordered = True
    order.save()
    cart.save()
    # update item sales type to Sold
    cart_lines = Cart_line.objects.filter(cart=cart)
    for line in cart_lines:
        item = line.item
        item.sales_type = "s"
        item.status = 'c'
        item.save()

    return JsonResponse({'url': 'orders'})


# Allows user to browse their cart
@require_http_methods(['GET', 'POST'])
@ensure_csrf_cookie
def cart(request):
    # Get the user's cart, if it doesn't exist, create it
    if not request.user.is_authenticated:
        if request.method == 'POST':
            return JsonResponse({"message": "auth"})
        else:
            return render(request, "ubs_project/merchandise/cart.html")

    try:
        cart = Cart.objects.filter(user=request.user).get(is_ordered=False)
    except Cart.DoesNotExist:
        cart = Cart(user=request.user)
        cart.save()

    if request.method == "POST":
        try:
            cart.add(request.POST['item_id'], 1)
            cart.save()
            return JsonResponse({"message": "success"})
        except Cart.error:
            return JsonResponse({"message": "error"})

    else:
        cart_lines = cart.lines.all()
        cart_total = cart.total()
        context = {
            "cart_lines": cart_lines,
            "cart_total": cart_total
        }
        return render(request, "ubs_project/merchandise/cart.html", context)


@require_http_methods(['POST'])
@login_required(login_url="login")
def update_cart_quantity(request, cart_line_id):
    cart_line = Cart_line.objects.get(id=cart_line_id)
    cart_line.updateQuantityTo(request.POST['quantity'])
    return JsonResponse({"url": '/cart'})


# Allows users to browse their last orders
@login_required(login_url="login")
def orders(request):
    orders = Order.objects.filter(cart__user=request.user)
    context = {
        "orders": orders
    }
    return render(request, "ubs_project/merchandise/orders.html", context)


# Allows the staff to browse all orders
@staff_member_required
def dashboard(request):
    # Get all orders and count them
    orders = Order.objects.all().order_by('-date')
    orders_count = orders.count()

    # Compute the mean amount of all orders
    orders_mean = 0
    for order in orders:
        orders_mean += order.total()
    orders_mean = round(orders_mean / orders_count, 2)

    # Get the orders of the day
    today_min = datetime.combine(datetime.today(), time.min)
    today_max = datetime.combine(datetime.today(), time.max)
    orders_today = Order.objects.filter(date__range=(today_min, today_max)).count()

    context = {
        "orders": orders,
        "orders_today": orders_today,
        "orders_count": orders_count,
        "orders_mean": orders_mean
    }
    return render(request, "ubs_project/merchandise/dashboard.html", context)


# Allows users to see details of one order
def order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.user.is_staff or (request.user.is_authenticated and request.user == order.cart.user):
        context = {
            "order": order,
            "order_lines": order.cart.lines.all(),
            "order_total": order.total()
        }
        return render(request, "ubs_project/merchandise/order.html", context)
    else:
        return render(request, "ubs_project/merchandise/error.html", {"message": "access is forbidden"}, 403)
