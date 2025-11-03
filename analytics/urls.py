from django.urls import path
from .views import SalesSummaryView, TopCustomersView, TopProductsView

urlpatterns = [
    path('sales-summary/', SalesSummaryView.as_view(), name='sales-summary'),
    path('top-customers/', TopCustomersView.as_view(), name='top-customers'),
    path('top-products/', TopProductsView.as_view(), name='top-products'),
]