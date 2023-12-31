# views.py
from django.http import JsonResponse
from .scrap_thread import scrap
import json
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .database import get_database
import bcrypt
# from .scraping import scraping_thread

# Get the database
dbase = get_database()



def search_and_scrape(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        search_text = data.get('searchText')
        try:
            # Scrape reviews using the utility function
            reviews = scrap(search_text)

            print ("views ma : " ,reviews)

            return JsonResponse({'title': reviews})


        except Exception as error:
            print("Error:", error)

    return JsonResponse({'error': 'Invalid request method'})



@api_view(['GET'])
def get_products(request, collection_name):
    try:
        # Dynamically set the collection name based on user input
        collection = dbase[collection_name]

        # Fetch products from the specified collection
        products = list(collection.find())

        # Serialize the data using ProductSerializer
        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def register_user(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            user_data = data.get('userData')

            if user_data is None:
                return JsonResponse({'error': 'User data is missing'})

            # Extract user details
            name = user_data.get('name')
            email = user_data.get('email')
            password = user_data.get('password')

            # Validate required fields
            if not (name and email and password):
                return JsonResponse({'error': 'Incomplete user data'})

            # Access the 'userInfo' collection
            user_info_collection = dbase['userInfo']

            # Check if email is already registered
            existing_user = user_info_collection.find_one({'email': email})
            if existing_user:
                return JsonResponse({'error': 'Email is already registered'})

            # Hash the password
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())

            # Prepare the document to be inserted
            user_document = {
                'name': name,
                'email': email,
                # Ensure to decode the hashed password
                'password': hashed_password.decode('utf-8'),
            }

            # Insert the document into the 'userInfo' collection
            user_info_collection.insert_one(user_document)

            return JsonResponse({'message': 'Registration successful'})

    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'error': 'Internal server error'})

    return JsonResponse({'error': 'Invalid request method'})


def signin_user(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            user_data = data.get('userData')

            if user_data is None:
                return JsonResponse({'error': 'User data is missing'})

            # Extract user details
            email = user_data.get('email')
            password = user_data.get('password')

            # Validate required fields
            if not (email and password):
                return JsonResponse({'error': 'Incomplete user data'})

            # Access the 'userInfo' collection
            user_info_collection = dbase['userInfo']

            # Check if email exists in the database
            user = user_info_collection.find_one({'email': email})
            if not user:
                return JsonResponse({'error': 'Email not registered'})

            # Verify the provided password against the stored hashed password
            stored_password = user.get('password')
            if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return JsonResponse({'error': 'Invalid password'})

            return JsonResponse({'message': 'Login successful'})

    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'error': 'Internal server error'})

    return JsonResponse({'error': 'Invalid request method'})
