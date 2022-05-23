try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf import urls

from django.urls import path
from project.apps.robokassa import views as v

from project.apps.shop.views import (CheckoutView, HomeView, OrderSummaryView,
                                     ProductDetailView, QiwiPayView,
                                     RoboPaymentView, StripePaymentView,
                                     add_to_cart, pay_with_robokassa,
                                     redirect_home_payment_error,
                                     redirect_home_payment_success,
                                     remove_from_cart,
                                     remove_single_item_from_cart)

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('payment/stripe/', StripePaymentView.as_view(), name="payment-stripe"),
    path('payment/qiwi/', QiwiPayView.as_view(), name="payment-qiwi"),
    path('payment/redirect/home/success', redirect_home_payment_success, name="redirect_home_payment_success"),
    path('payment/redirect/home/error', redirect_home_payment_error, name="redirect_home_payment_error"),
    path('payment/robokassa/', pay_with_robokassa, name="payment-robo"),
    path('payment/robokassa/result/', v.receive_result, name='robokassa_result'),
    path('payment/robokassa/success/', v.success, name='robokassa_success'),
    path('payment/robokassa/fail/', v.fail, name='robokassa_fail'),
]
