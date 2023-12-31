# products/urls.py
from django.urls import path
from .views import search_and_scrape, get_products, register_user, signin_user, nlp_view, get_summary_text, get_user_details,update_userdetails
urlpatterns = [
    path('api/search_and_scrape/', search_and_scrape, name='search_and_scrape'),
    path('api/get_products/<str:collection_name>/',
         get_products, name='get_products'),
    path('api/register/', register_user, name='register_user'),
    path('api/signin/', signin_user, name='signin_user'),
    path('api/nlp_view/<str:product_name>/', nlp_view, name='nlp_view'),
    path('api/summarize/<str:product_name>/',
         get_summary_text, name='get_summary_text'),
    path('api/userdetails/<str:user_id>/',
         get_user_details, name='get_user_details'),
    path('api/update_userdetails/<str:user_id>/',
         update_userdetails, name='update_userdetails')
]
