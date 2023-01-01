from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'pr_name', 'pr_amount', 'pr_cost', 'pr_description', 'pr_image', 'pr_date'
        ]
