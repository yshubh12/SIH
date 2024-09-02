from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.db.models import Q
from django.core.paginator import Paginator
from carts.views import _cart_id
from carts.models import Cart, CartItem


def store(request, category_slug=None):
    # Handle normal and featured products (all in Product model now)
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
    else:
        products = Product.objects.filter(is_available=True).order_by('id')

    paginator = Paginator(products, 6)  # Adjust the number per page as needed
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    products = Product.objects.filter(
        Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
    ).order_by('-created_date') if keyword else Product.objects.none()

    paginator = Paginator(products, 6)  # Adjust the number per page as needed
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
