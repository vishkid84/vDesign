from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, current_bag in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += current_bag * product.price
        product_count += current_bag
        bag_items.append({
            'item_id': item_id,
            'current_bag': current_bag,
            'product': product
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context