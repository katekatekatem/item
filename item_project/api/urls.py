from django.urls import path

from . import views


urlpatterns = [
    path(
        'buy/<int:item_id>/',
        views.get_checkout_session,
        name='get_checkout_session'
    ),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
