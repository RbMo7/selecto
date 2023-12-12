# views.py
from django.http import JsonResponse
from .reviews_scrap import get_reviews_amazon
import json


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
