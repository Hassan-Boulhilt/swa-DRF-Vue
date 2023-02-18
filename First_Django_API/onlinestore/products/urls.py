from django.urls import path
from .views import product_list, product_detail,manufacturers_list, manufacturer_detail

urlpatterns=[
    path("", product_list, name="product-list"),
    path("product/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturers/", manufacturers_list, name="manufacturers-list"),
    path("manufacturer/<int:pk>", manufacturer_detail, name="manufacturer-detail")
]