from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def products(request):

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    
    template = 'products/product_detail.html'

    context = {
        'product': product,
    }

    return render(request, template, context)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)