# serializers.py
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_img = serializers.URLField()

    def to_representation(self, instance):
        return {
            'product_name': instance.get('product_name'),
            'product_img': instance.get('product_img'),
            "product_price": instance.get('product_price')
        }


class UserSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_img = serializers.URLField()
    name = serializers.CharField()
    email = serializers.CharField()
    def to_representation(self, instance):
        return {
            'name': instance.get('name'),
            'email': instance.get('email'),
        }