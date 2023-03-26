from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from track_order.models import Order
def order_index(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'order_index.html', context)
def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        'order': order
    }
    return render(request, 'order_detail.html', context)
def make_fav(request, pk):
    order = Order.objects.get(pk=pk)
    order.isFav=True
    order.save()
    return HttpResponseRedirect(reverse('order_index'))


