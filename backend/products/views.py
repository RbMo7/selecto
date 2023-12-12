# views.py
from django.http import JsonResponse
from .reviews_scrap import get_reviews_amazon
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .database import get_database

dbase = get_database()

def search_and_scrape(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        search_text = data.get('searchText')
        try:
            # Scrape reviews using the utility function
            reviews = get_reviews_amazon(search_text)

        except Exception as error:
            print("Error:", error)

    return JsonResponse({'error': 'Invalid request method'})
    
    
# @api_view(['GET'])
@api_view(['GET'])
def get_products(request, collection_name):
    try:
        # Dynamically set the collection name based on user input
        collection = dbase[collection_name]

        # Fetch products from the specified collection
        products = list(collection.find())

        # Serialize the data and return the response
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

