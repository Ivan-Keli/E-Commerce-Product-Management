from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, Category


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            price=price,
            category=category,
            description=description,
            image=image
        )
        return redirect("list_products")

    categories = Category.objects.all()
    return render(request, "products/add_product.html", {"categories": categories})


def list_products(request):
    products = Product.objects.all()

    return render(request, "products/list_product.html", {"products": products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "products/product_detail.html", {"product": product})

