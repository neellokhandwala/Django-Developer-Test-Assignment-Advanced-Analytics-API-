#!/usr/bin/env python
"""
Sample data creation script for testing the Sales Analytics API
Run this after migrations: python sample_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_analytics.settings')
django.setup()

from core.models import Customer, Product, Order, OrderItem
from decimal import Decimal


def create_sample_data():
    print("Creating sample data...")
    
    # Create customers
    customers = [
        Customer.objects.create(name="John Doe", email="john@example.com"),
        Customer.objects.create(name="Jane Smith", email="jane@example.com"),
        Customer.objects.create(name="Bob Johnson", email="bob@example.com"),
        Customer.objects.create(name="Alice Brown", email="alice@example.com"),
        Customer.objects.create(name="Charlie Wilson", email="charlie@example.com"),
    ]
    
    # Create products
    products = [
        Product.objects.create(name="Laptop", price=Decimal("999.99")),
        Product.objects.create(name="Mouse", price=Decimal("29.99")),
        Product.objects.create(name="Keyboard", price=Decimal("79.99")),
        Product.objects.create(name="Monitor", price=Decimal("299.99")),
        Product.objects.create(name="Headphones", price=Decimal("149.99")),
    ]
    
    # Create orders with items
    orders_data = [
        (customers[0], [(products[0], 1), (products[1], 2)]),  # John: Laptop + 2 Mice
        (customers[1], [(products[2], 1), (products[3], 1)]),  # Jane: Keyboard + Monitor
        (customers[2], [(products[4], 2)]),                    # Bob: 2 Headphones
        (customers[0], [(products[1], 3), (products[2], 1)]),  # John: 3 Mice + Keyboard
        (customers[3], [(products[0], 1), (products[3], 2)]),  # Alice: Laptop + 2 Monitors
        (customers[4], [(products[4], 1), (products[1], 1)]),  # Charlie: Headphones + Mouse
    ]
    
    for customer, items in orders_data:
        order = Order.objects.create(customer=customer)
        for product, quantity in items:
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
    
    print(f"Created {len(customers)} customers")
    print(f"Created {len(products)} products")
    print(f"Created {len(orders_data)} orders")
    print("Sample data creation completed!")


if __name__ == "__main__":
    create_sample_data()