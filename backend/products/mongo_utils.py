# mongo_utils.py

from pymongo import MongoClient

def get_mongo_database():
    # Provide the MongoDB connection string
    connection_string = "mongodb+srv://RbMo:tCap11fDEdXi68PW@reviews-list.q56a6p2.mongodb.net/"

    # Create a connection using MongoClient
    client = MongoClient(connection_string)

    # Return the MongoDB database
    return client.get_database()

# You can define other functions for MongoDB operations in this module
