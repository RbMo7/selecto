# views.py
from django.http import JsonResponse
from .scraping_utils import scrape_reviews
import json

def search_and_scrape(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        search_text = data.get('searchText')

        print(search_text)

        try:
            # Scrape reviews using the utility function
            reviews = scrape_reviews(search_text)
            
        except Exception as error:
            print("i am here")
            print("Error:", error)

    return JsonResponse({'error': 'Invalid request method'})
