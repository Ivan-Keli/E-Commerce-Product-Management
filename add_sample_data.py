"""
Script to add sample products and categories
Run: python add_sample_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Product

# Create categories
categories_data = ['Electronics', 'Clothing', 'Books', 'Home & Garden']

print("Creating categories...")
for cat_name in categories_data:
    category, created = Category.objects.get_or_create(name=cat_name)
    if created:
        print(f"✓ Created category: {cat_name}")
    else:
        print(f"- Category already exists: {cat_name}")

# Create sample products
products_data = [
    {
        'name': 'Laptop',
        'category': 'Electronics',
        'price': 45000.00,
        'description': 'High-performance laptop with 16GB RAM and 512GB SSD'
    },
    {
        'name': 'Smartphone',
        'category': 'Electronics',
        'price': 25000.00,
        'description': 'Latest smartphone with amazing camera and long battery life'
    },
    {
        'name': 'T-Shirt',
        'category': 'Clothing',
        'price': 1500.00,
        'description': 'Comfortable cotton t-shirt available in multiple colors'
    },
    {
        'name': 'Jeans',
        'category': 'Clothing',
        'price': 3500.00,
        'description': 'Classic denim jeans with perfect fit'
    },
    {
        'name': 'Python Programming Book',
        'category': 'Books',
        'price': 2500.00,
        'description': 'Comprehensive guide to Python programming for beginners'
    },
    {
        'name': 'Garden Tools Set',
        'category': 'Home & Garden',
        'price': 4500.00,
        'description': 'Complete set of essential gardening tools'
    },
]

print("\nCreating products...")
for product_data in products_data:
    category = Category.objects.get(name=product_data['category'])
    product, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults={
            'category': category,
            'price': product_data['price'],
            'description': product_data['description']
        }
    )
    if created:
        print(f"✓ Created product: {product_data['name']}")
    else:
        print(f"- Product already exists: {product_data['name']}")

print(f"\n✅ Done! Total categories: {Category.objects.count()}")
print(f"✅ Total products: {Product.objects.count()}")
print("\nVisit http://127.0.0.1:8000/ to see your products!")
