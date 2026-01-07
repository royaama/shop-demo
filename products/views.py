import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def product_api(request):
    # we want to see the products (GET)
    if request.method == 'GET':
        products = Product.objects.all().values()
        return JsonResponse(list(products), safe=False)
    # we want to create a new product (POST)
    if request.method == 'POST':
        # we read the data sent in the request body
        data = json.loads(request.body)
        # we create a new product in the database
        new_product = Product.objects.create(
            title=data['title'],
            price=data['price'],
            stock=data['stock']
        )
        # we return a response indicating success
        return JsonResponse({'message': 'Product created!', 'id': new_product.id})