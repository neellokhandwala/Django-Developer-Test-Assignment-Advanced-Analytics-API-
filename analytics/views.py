from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, F
from django.utils.dateparse import parse_date
from core.models import Order, Customer, Product, OrderItem
from decimal import Decimal


class SalesSummaryView(APIView):
    def get(self, request):
        # Date filtering
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')
        
        orders_qs = Order.objects.all()
        if from_date:
            from_date = parse_date(from_date)
            if from_date:
                orders_qs = orders_qs.filter(order_date__date__gte=from_date)
        
        if to_date:
            to_date = parse_date(to_date)
            if to_date:
                orders_qs = orders_qs.filter(order_date__date__lte=to_date)

        # Calculate total sales
        total_sales = OrderItem.objects.filter(
            order__in=orders_qs
        ).aggregate(
            total=Sum(F('quantity') * F('product__price'))
        )['total'] or Decimal('0.00')

        # Count customers and products
        total_customers = Customer.objects.count()
        total_products_sold = OrderItem.objects.filter(
            order__in=orders_qs
        ).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        return Response({
            'total_sales': total_sales,
            'total_customers': total_customers,
            'total_products_sold': total_products_sold
        })


class TopCustomersView(APIView):
    def get(self, request):
        # Date filtering
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')
        
        orders_qs = Order.objects.all()
        if from_date:
            from_date = parse_date(from_date)
            if from_date:
                orders_qs = orders_qs.filter(order_date__date__gte=from_date)
        
        if to_date:
            to_date = parse_date(to_date)
            if to_date:
                orders_qs = orders_qs.filter(order_date__date__lte=to_date)

        top_customers = Customer.objects.filter(
            order__in=orders_qs
        ).annotate(
            total_spent=Sum(F('order__items__quantity') * F('order__items__product__price'))
        ).order_by('-total_spent')[:5]

        data = []
        for customer in top_customers:
            data.append({
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'total_spent': customer.total_spent or Decimal('0.00')
            })

        return Response(data)


class TopProductsView(APIView):
    def get(self, request):
        # Date filtering
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')
        
        orders_qs = Order.objects.all()
        if from_date:
            from_date = parse_date(from_date)
            if from_date:
                orders_qs = orders_qs.filter(order_date__date__gte=from_date)
        
        if to_date:
            to_date = parse_date(to_date)
            if to_date:
                orders_qs = orders_qs.filter(order_date__date__lte=to_date)

        top_products = Product.objects.filter(
            orderitem__order__in=orders_qs
        ).annotate(
            total_sold=Sum('orderitem__quantity')
        ).order_by('-total_sold')[:5]

        data = []
        for product in top_products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'total_sold': product.total_sold or 0
            })

        return Response(data)