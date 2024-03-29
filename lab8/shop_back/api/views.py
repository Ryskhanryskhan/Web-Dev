from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from api.models import Category, Product
def products_list(request):
    products = Product.objects.all()
    product_json = list(product.to_json() for product in products)
    return JsonResponse(product_json, safe = False)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id = product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status = 400)
    
    return JsonResponse(product.to_json())

def categories_list(request):
    categories = Category.objects.all()
    category_json = list(category.to_json() for category in categories)
    return JsonResponse(category_json, safe=False)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status = 400)
    
    return JsonResponse(category.to_json())

def categories_products(self, category_id):
   try:
      category = Category.objects.get(id=category_id)
   except Category.DoesNotExist as e:
      return JsonResponse({'message': str(e)}, status=400)
   
   products = [product.to_json() for product in category.products.all()]
   return JsonResponse(products,safe = False)