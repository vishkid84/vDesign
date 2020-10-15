from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    current_bag = int(request.POST.get('current_bag'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = current_bag
    
    request.session['bag'] = bag

    return redirect(redirect_url)