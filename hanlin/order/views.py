from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import admin_required
# Create your views here.

@login_required
def order(request):
    orders = Order.objects.all()
    context = {'orders':orders, 'userOrders':Order.objects.filter(customer=request.user)}
    return render(request, 'order/order.html', context)

@admin_required
def orderDelete(request, orderId):
    if request.method == 'GET':
        return order(request)
    #POST
    order = get_object_or_404(Order, id=orderId)
    order.plant.buyes.remove(order.customer)
    order.plant.inventory = order.plant.inventory+1
    order.plant.save()
    order.delete()
    messages.success(request, '訂單已取消')
    return redirect('order:order')


