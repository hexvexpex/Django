from django.urls import path

from products.views import ProductListCreateAPIView, ProductRUDAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name="products_list_create"),
    # pk - id, just should be written like this
    path('products/<int:pk>/', ProductRUDAPIView.as_view(), name="products_RUD"),
]
