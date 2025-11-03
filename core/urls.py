from django.urls import path
from .views import CustomerListCreateView, ProductListCreateView, OrderListCreateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]