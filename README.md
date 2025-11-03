<<<<<<< HEAD
# Sales Analytics API

A Django REST Framework API for sales analytics with JWT authentication.

## Features

- Customer, Product, Order, and OrderItem management
- Nested order creation with items
- Analytics endpoints for sales summary, top customers, and top products
- JWT authentication
- Date range filtering for analytics
- Optimized database queries
- Input validation and business rules

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /api/token/` - Get JWT access token
- `POST /api/token/refresh/` - Refresh JWT token

### Core Endpoints
- `GET/POST /api/customers/` - List or create customers
- `GET/POST /api/products/` - List or create products
- `GET/POST /api/orders/` - List or create orders (with nested items)

### Analytics Endpoints
- `GET /api/analytics/sales-summary/` - Get total sales, customers, products sold
- `GET /api/analytics/top-customers/` - Get top 5 customers by purchase amount
- `GET /api/analytics/top-products/` - Get top 5 most sold products

### Date Range Filtering

Analytics endpoints support date filtering:
```
GET /api/analytics/sales-summary/?from=2024-01-01&to=2024-12-31
```

## Example API Requests

### 1. Get JWT Token

```json
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. Create Customer

```json
POST /api/customers/
Authorization: Bearer <access_token>
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

### 3. Create Product

```json
POST /api/products/
Authorization: Bearer <access_token>
{
    "name": "Laptop",
    "price": "999.99"
}
```

### 4. Create Order with Items

```json
POST /api/orders/
Authorization: Bearer <access_token>
{
    "customer": 1,
    "items": [
        {
            "product": 1,
            "quantity": 2
        },
        {
            "product": 2,
            "quantity": 1
        }
    ]
}
```

**Response:**
```json
{
    "id": 1,
    "customer": 1,
    "customer_name": "John Doe",
    "order_date": "2024-01-15T10:30:00Z",
    "items": [
        {
            "id": 1,
            "product": 1,
            "product_name": "Laptop",
            "product_price": "999.99",
            "quantity": 2,
            "item_total": "1999.98"
        }
    ],
    "total_price": "1999.98"
}
```

### 5. Get Sales Summary

```json
GET /api/analytics/sales-summary/
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "total_sales": "15000.00",
    "total_customers": 25,
    "total_products_sold": 150
}
```

### 6. Get Top Customers

```json
GET /api/analytics/top-customers/
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "total_spent": "2500.00"
    }
]
```

### 7. Get Top Products

```json
GET /api/analytics/top-products/
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Laptop",
        "price": "999.99",
        "total_sold": 25
    }
]
```

## Testing

Run the unit tests:

```bash
python manage.py test
```

## Business Rules

- Quantity must be ≥ 1
- Each order must have at least one item
- Email addresses must be unique for customers
- JWT authentication required for all endpoints

## Database Schema

- **Customer**: id, name, email (unique), joined_on
- **Product**: id, name, price
- **Order**: id, customer (FK), order_date
- **OrderItem**: id, order (FK), product (FK), quantity (≥1)

## Performance Optimizations

- Uses `select_related()` and `prefetch_related()` for efficient queries
- Database-level aggregations for analytics
- Proper indexing on foreign keys
=======
# Django-Developer-Test-Assignment-Advanced-Analytics-API-
Build a small Sales Analytics API using Django REST Framework.  This test checks your ability to design models, write analytics queries, and structure APIs.
>>>>>>> 1aa16d1ab994d3cafa378911dc735710410797cd
