from django.shortcuts import render, get_object_or_404, redirect
from marketplace.models import Artwork
from .models import Order, OrderItem

# Create your views here.

def create_order(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)

    order = Order.objects.create(
        user=request.user,
        total=artwork.price,
        shipping_address="Dirección de prueba"
    )

    OrderItem.objects.create(
        order=order,
        artwork=artwork,
        price=artwork.price
    )

    # marcar como pagado (simulación)
    order.status = 'paid'
    order.save()

    return redirect('order_detail', order.id)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/detail.html', {'order': order})
