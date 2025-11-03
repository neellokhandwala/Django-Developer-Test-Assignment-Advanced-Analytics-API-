from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Customer, Product, Order, OrderItem
from decimal import Decimal


class SalesSummaryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create test user for JWT authentication
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Get JWT token
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        # Create test data
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com'
        )
        
        self.product1 = Product.objects.create(
            name='Product 1',
            price=Decimal('10.00')
        )
        
        self.product2 = Product.objects.create(
            name='Product 2',
            price=Decimal('20.00')
        )
        
        self.order = Order.objects.create(customer=self.customer)
        
        OrderItem.objects.create(
            order=self.order,
            product=self.product1,
            quantity=2
        )
        
        OrderItem.objects.create(
            order=self.order,
            product=self.product2,
            quantity=1
        )

    def test_sales_summary(self):
        url = reverse('sales-summary')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.data
        self.assertEqual(data['total_sales'], Decimal('40.00'))  # (2*10) + (1*20)
        self.assertEqual(data['total_customers'], 1)
        self.assertEqual(data['total_products_sold'], 3)  # 2 + 1

    def test_sales_summary_with_date_filter(self):
        url = reverse('sales-summary')
        response = self.client.get(url, {'from': '2024-01-01', 'to': '2024-12-31'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.data
        self.assertEqual(data['total_sales'], Decimal('40.00'))
        self.assertEqual(data['total_customers'], 1)
        self.assertEqual(data['total_products_sold'], 3)