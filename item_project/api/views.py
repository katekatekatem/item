import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from item.models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_KEY


def get_checkout_session(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000/api/success/',
        cancel_url='http://localhost:8000/api/cancel/',
    )
    return JsonResponse({'session_id': session.id})


def get_order_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': order.get_currency(),
                    'product_data': {
                        'name': f'Order #{order.id}',
                    },
                    'unit_amount': int(order.get_total_price() * 100),
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000/api/success/',
        cancel_url='http://localhost:8000/api/cancel/',
    )
    return JsonResponse({'session_id': session.id})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'item_page.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_page.html', context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'
