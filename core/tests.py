from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Customer, Product, Order, OrderItem
from decimal import Decimal


class ModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com'
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('10.00')
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'Test Customer')
        self.assertEqual(self.customer.email, 'test@example.com')
        self.assertTrue(self.customer.joined_on)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, Decimal('10.00'))

    def test_order_creation(self):
        order = Order.objects.create(customer=self.customer)
        self.assertEqual(order.customer, self.customer)
        self.assertTrue(order.order_date)

    def test_order_item_validation(self):
        order = Order.objects.create(customer=self.customer)
        
        # Valid order item
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=2
        )
        self.assertEqual(order_item.quantity, 2)
        
        # Invalid quantity
        with self.assertRaises(ValidationError):
            invalid_item = OrderItem(
                order=order,
                product=self.product,
                quantity=0
            )
            invalid_item.full_clean()