from django.urls import path

from products.views import ProductListCreateAPIView, ProductRUDAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk:>/', ProductRUDAPIView.as_view()),
]
