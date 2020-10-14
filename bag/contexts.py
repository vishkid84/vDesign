from django.conf import settings

def bag_contents(request):

    bag_items = []
    grand_total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context