# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','product_img']
        extra_kwargs = {'product_name': {'required': False}, 'product_img': {'required': False}}
