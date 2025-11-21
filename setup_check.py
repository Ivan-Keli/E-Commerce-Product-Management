"""
Quick setup verification script
Run this after migrations to verify everything is working
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Product

print("✓ Django setup successful")
print("✓ Models imported successfully")
print(f"✓ Categories in database: {Category.objects.count()}")
print(f"✓ Products in database: {Product.objects.count()}")
print("\nSetup verification complete!")
print("\nNext steps:")
print("1. Run: python manage.py createsuperuser")
print("2. Run: python manage.py runserver")
print("3. Visit: http://127.0.0.1:8000/")
