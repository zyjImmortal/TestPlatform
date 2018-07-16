from django.shortcuts import render

# Create your views here.
from product.models import Product


def product_manage(request):
    username = request.session.get('user')
    products = Product.objects.all()
    return render(request, 'product_manage.html', {"user":username, "products":products})