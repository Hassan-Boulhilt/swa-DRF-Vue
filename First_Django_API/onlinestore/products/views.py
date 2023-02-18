from django.http import JsonResponse


# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())} #"pk", "name"
    response = JsonResponse(data)
    return response
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)

        data = {"product":{"name": product.name,
                            "description": product.description,
                            "photo": product.photo.url,
                            "price": product.price,
                            "quantity": product.quantity,
                            "shipping": product.shipping(),
                            "total cost": product.totalcost(),
                        }
            }
        response = JsonResponse(data)
    except:

        response =  JsonResponse({"error":{
            "code": 404,
            "message": "Product not found!"
        }},status= 404)
    return response

def manufacturers_list(request):
    manufacturers = Manufacturer.objects.all()
    data ={ "manufacturers": list(manufacturers.values())}
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk= pk)
        data = {"manufacturer":{
                                "name": manufacturer.name,
                                "location": manufacturer.location
                            }
            }
        response = JsonResponse(data)
    except:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message": "Manufacturer not found",
            }
        }, status=404)
    return response



# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"


