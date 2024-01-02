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
    

class TopCollectionSerializer(serializers.Serializer):
    collection = serializers.CharField()
    count = serializers.IntegerField()

class TopCollectionsResponseSerializer(serializers.Serializer):
    top_collections = TopCollectionSerializer(many=True)
    def to_representation(self, instance):
        return {'top_collections': instance['top_collections']}