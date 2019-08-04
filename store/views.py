from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def all_products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category = category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'store/all_products.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    images = product.images.all()
    context = {
        'product':product,
        'cart_product_form':cart_product_form,
        'images': images,
    }

    return render(request, 'store/detail_product.html', context)
