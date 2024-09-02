from django.shortcuts import render
from store.models import Product, FeaturedProduct

def home(request):
    fproducts = FeaturedProduct.objects.all().filter(is_available=True)

    context = {
        'fproducts': fproducts,
    }
    return render(request,'home.html',context)