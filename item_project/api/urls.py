from django.urls import path

from . import views


urlpatterns = [
    path(
        'buy/<int:item_id>/',
        views.get_checkout_session,
        name='get_checkout_session'
    ),
    path(
        'buy_order/<int:order_id>/',
        views.get_order_checkout_session,
        name='get_order_checkout_session'
    ),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
