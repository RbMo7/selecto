# products/urls.py
from django.urls import path
from .views import search_and_scrape

urlpatterns = [
    path('api/search_and_scrape/', search_and_scrape, name='search_and_scrape'),
]
