from django.shortcuts import render
from .models import Product

def home(request):
    services = [
        ("Animal Rearing", "High-quality livestock raised with care."),
        ("Fresh Harvest", "Organic crops picked daily from our fields."),
        ("Preparation", "Professional harvesting and cleaning services."),
        ("Delivery/Pickup", "Fast delivery to your door or easy pickup.")
    ]
    steps = ["Browse Products", "Place Order", "We Prepare", "Delivery/Pickup"]
    return render(request, 'home.html', {'services': services, 'steps': steps})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})