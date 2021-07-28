from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_bag(request):
    """ SHOWS ALL CONTENTS IN SHOPPING BAG """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ ALLOWS USERS TO ADD SPECIFIC PRODUCTS
    TO SHOPPING BAG INCLUDING QUANTITY OF ITEMS """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated quantity of {product.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Successfully added {product.name} to shopping bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ ADJUSTS QUANTITY OF SPECIFIC ITEM """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {product.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from shopping bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ REMOVES SELECTED ITEM FROM SHOPPING BAG """

    product = Product.objects.get(pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        messages.info(
            request, f'Removed {product.name} from shopping bag.')
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    
    except Exception as e:
        messages.error(request, f'Error removing item. Error: {e}')
        return HttpResponse(status=500)
