from django.shortcuts import render
from testapp.models import Product

def product_list(request):
    products = Product.objects.all()
    context = {
        "product_list": products,
    }
    return render(
        request,
        "testapp/product_list.html",
        context=context,
    )

def get_product_by_id(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(
        request,
        "testapp/product_info.html",
        context=context
    )