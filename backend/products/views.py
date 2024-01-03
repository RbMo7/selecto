# views.py
from django.http import JsonResponse
from .scrap_thread import scrap
import json
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer, UserSerializer, TopCollectionsResponseSerializer
from .database import get_database
import bcrypt
from .nlp import process_nlp_collection
from .summaryfinal import summarize
from bson import ObjectId
# from .Nlpfinal import get_data_from_mongodb, tokenize_and_analyze_sentiment, analyze_with_roberta, get_summary, cut_text_into_sentences
# from .scraping import scraping_thread

# Get the database

def search_and_scrape(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        search_text = data.get('searchText')
        try:
            # Scrape reviews using the utility function
            reviews = scrap(search_text)

            print("views ma : ", reviews)

            return JsonResponse({'title': reviews})

        except Exception as error:
            print("Error:", error)

    return JsonResponse({'error': 'Invalid request method'})


@api_view(['GET'])
def get_products(request, collection_name):
    try:
        database_name='Reviews'
        dbase = get_database(database_name)
        # print("yeta ta aayo")
        # Dynamically set the collection name based     on user input
        collection = dbase[collection_name]

        # Fetch products from the specified collection
        products = list(collection.find())

        # Serialize the data using ProductSerializer
        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
def nlp_view(request, product_name):
    
    try:
        # Call the existing NLP processing function
        print("printing collection in views:", product_name)
        avg_positive, avg_negative, avg_neutral = process_nlp_collection(product_name)
        summary = summarize(product_name)

        nlp=[avg_positive, avg_negative, avg_neutral,summary]
        
        print (avg_negative)
        print (avg_neutral)
        print (avg_positive)
        print (nlp)

        # Return the results as JSON
        return JsonResponse({
            'nlp': nlp
        })
    except Exception as e:
        # Handle any exceptions and return an error response
        return JsonResponse({'error': str(e)}, status=500)

    
def get_summary_text(request, product_name):

    try:
        # Call the existing NLP processing function
        summary = summarize(product_name)

        # Return the results as JSON
        return JsonResponse({
            'summary': summary
        })
    except Exception as e:
        # Handle any exceptions and return an error response
        return JsonResponse({'error': str(e)}, status=500)


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
            database_name='Users'
            dbase = get_database(database_name)
            user_info_collection = dbase['userInfo']

            # Check if email is already registered
            existing_user = user_info_collection.find_one({'email': email})
            if existing_user:
                return JsonResponse({'error': 'Email is already registered'})

            # Hash the password
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())

            # Set a default image URL or binary data
            default_image_url = 'C:\My Files\KU\4th sem\Project\selecto\frontend\src\Components\Images\defaultuser.png'
            
            # Prepare the document to be inserted
            user_document = {
                'name': name,
                'email': email,
                'password': hashed_password.decode('utf-8'),
                'profile_image': default_image_url,  
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
            database_name='Users'
            dbase = get_database(database_name)
            user_info_collection = dbase['userInfo']

            # Check if email exists in the database
            user = user_info_collection.find_one({'email': email})
            if not user:
                return JsonResponse({'error': 'Email not registered'})

            # Verify the provided password against the stored hashed password
            stored_password = user.get('password')
            if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return JsonResponse({'error': 'Invalid password'})
            
            user_id = str(user.get('_id'))

            # Create a dictionary for the response

            print(user_id)
            return JsonResponse({'user_id': user_id})

    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'error': 'Internal server error'})

    return JsonResponse({'error': 'Invalid request method'})
# Your utility function to get hot products
def get_hot_products():
    try:
        database_name = 'Reviews'
        dbase = get_database(database_name)
        list_of_collection = dbase.list_collection_names()
        collection_counts = []
        
        for collection_name in list_of_collection:
            current_collection = dbase[collection_name]
            res = current_collection.find_one()
            count = res['count']
            img = res['product_img']
            collection_counts.append({'collection': collection_name,'product_img': img, 'count': count})

        sorted_col = sorted(collection_counts, key=lambda x: x['count'], reverse=True)
        top_5_collections = sorted_col[:5]

        return {'top_collections': top_5_collections}

    except Exception as e:
        return {'error': str(e)}


# Your DRF view for hot products
@api_view(['GET'])
def hot_products(request):
    hot_products_data = get_hot_products()
    serializer = TopCollectionsResponseSerializer(hot_products_data)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_user_details(request, user_id):
    try:
        database_name = 'Users'
        dbase = get_database(database_name)

        # Dynamically set the collection name based on user input
        collection = dbase["userInfo"]

        # Fetch user from the specified collection
        print("user id is:", user_id)
        user = collection.find_one({"_id": ObjectId(user_id)})
        print("naam ho:", user)

        if not user:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the data using UserSerializer
        serializer = UserSerializer(user)
        hot_products_data = get_hot_products()
        return Response({'user': serializer.data, 'hot_products': hot_products_data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def update_userdetails(request, user_id):
    try:
        print("Updating user details")
        data = json.loads(request.body.decode('utf-8'))
        user_data = data.get('updatedUserDetails')
        print(user_data)

        # Select the database and collection
        database_name = 'Users'
        dbase = get_database(database_name)
        collection = dbase["userInfo"]

        # Extract the updated user details from the request data
        updated_user_details = {
            'name': user_data.get('name'),
            'email': user_data.get('email'),
            # Add other fields as needed
        }
        print(updated_user_details)

        # Update user details in the collection
        collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user_details})

        return Response({'message': 'User details updated successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



