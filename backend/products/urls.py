# products/urls.py
from django.urls import path
from .views import search_and_scrape, get_products

urlpatterns = [
    path('api/search_and_scrape/', search_and_scrape, name='search_and_scrape'),
    path('api/get_products/<str:collection_name>/', get_products, name='get_products'),
]
