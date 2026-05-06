from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from marketplace.models import Artwork
from .models import Order, OrderItem

# Create your views here.

@login_required
def create_order(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)

    if artwork.stock <= 0:
        return redirect('artwork_list')

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

    artwork.stock -= 1

    if artwork.stock == 0:
        artwork.is_available = False

    artwork.save()

    # marcar como pagado (simulación)
    order.status = 'paid'
    order.save()

    return redirect('order_detail', order.id)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/detail.html', {'order': order})
