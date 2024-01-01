# import pandas as pd
# import nltk
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from scipy.special import softmax
# from .database import get_database

# db = get_database()

# def process_nlp_collection(collection):
#     # Retrieve the data from the collection
#     data = list(collection.find())

#     # Create a DataFrame for tabular representation
#     df = pd.DataFrame(data)

#     # Initialize NLTK
#     nltk.download('punkt')
#     nltk.download('averaged_perceptron_tagger')
#     nltk.download('maxent_ne_chunker')
#     nltk.download('words')
#     nltk.download('vader_lexicon')

#     # Initialize sentiment analysis model
#     MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
#     tokenizer = AutoTokenizer.from_pretrained(MODEL)
#     model = AutoModelForSequenceClassification.from_pretrained(MODEL)

#     # Iterate over DataFrame rows and add sentiment scores
#     for i, row in df.iterrows():
#         text = str(row['Review'])  # Convert to string

#         # Assuming you have a function polarity_scores_roberta that returns a dictionary of sentiment scores
#         def polarity_scores_roberta(text):
#             encoded_text = tokenizer([text], return_tensors='pt', padding=True, truncation=True, max_length=512)
#             output = model(**encoded_text)
#             scores = softmax(output.logits[0].detach().numpy())
#             return {'roberta_pos': scores[0], 'roberta_neu': scores[1], 'roberta_neg': scores[2]}

#         scores_dict = polarity_scores_roberta(text)

#         # Add scores to the DataFrame
#         for score_name, score_value in scores_dict.items():
#             df.at[i, score_name] = score_value

#     # Group data by ObjectId and calculate average sentiment percentages
#     data = []

#     for ObjectId, group in df.groupby("_id"):
#         row_total = group['roberta_neg'].sum() + group['roberta_neu'].sum() + group['roberta_pos'].sum()

#         if row_total > 0:
#             positive_percentage = (group['roberta_pos'].sum() / row_total) * 100
#             neutral_percentage = (group['roberta_neu'].sum() / row_total) * 100
#             negative_percentage = (group['roberta_neg'].sum() / row_total) * 100

#             rounded_positive = round(positive_percentage, 1)
#             rounded_neutral = round(neutral_percentage, 1)
#             rounded_negative = round(negative_percentage, 1)

#             data.append({
#                 "_id": ObjectId,
#                 "Positive (%)": rounded_positive,
#                 "Neutral (%)": rounded_neutral,
#                 "Negative (%)": rounded_negative
#             })

#     # Create a DataFrame from the data
#     df_table = pd.DataFrame(data)

#     # Calculate average values
#     average_negative = df_table["Negative (%)"].mean()
#     average_neutral = df_table["Neutral (%)"].mean()
#     average_positive = df_table["Positive (%)"].mean()

#     print (average_negative, average_neutral, average_positive)

#     return average_negative, average_neutral, average_positive

# # usage:

# # collection_name = 'Pixel 7a - 128GB - Charcoal Pixel Buds A-Series - Charcoal'
# # collection = db[collection_name]
# # avg_negative, avg_neutral, avg_positive = process_nlp_collection(collection)
# # print("Average Negative Percentage:", avg_negative)
# # print("Average Neutral Percentage:", avg_neutral)
# # print("Average Positive Percentage:", avg_positive)


# -*- coding: utf-8 -*-
"""Untitled3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D3diqgQy7_H2qRN0fHewbaxW7N36I6k8
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
# !pip install pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax



def process_nlp_collection(title):
    uri = "mongodb+srv://selecto:DmdSvpAnRnudk1Zj@reviews-list.q56a6p2.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print('yeta ko error : ', e)

    plt.style.use('ggplot')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('vader_lexicon')

    print(title)

    # db=connectdb()
    db = client['Reviews']
    collection_names = db.list_collection_names()
    db = client['Reviews']
    collection = db[title]
    cursor = collection.find().limit(20)

    data = list(collection.find())

    df = pd.DataFrame(data)

    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    for i, row in df.iterrows():
        text = str(row['Review'])

        def polarity_scores_roberta(text):
            encoded_text = tokenizer(
                [text], return_tensors='pt', padding=True, truncation=True, max_length=512)
            output = model(**encoded_text)
            scores = softmax(output.logits[0].detach().numpy())
            return {'roberta_pos': scores[0], 'roberta_neu': scores[1], 'roberta_neg': scores[2]}

        scores_dict = polarity_scores_roberta(text)
        for score_name, score_value in scores_dict.items():
            df.at[i, score_name] = score_value
        data = []

        for ObjectId, group in df.groupby("_id"):
            row_total = group['roberta_neg'].sum(
            ) + group['roberta_neu'].sum() + group['roberta_pos'].sum()

            if row_total > 0:
                positive_percentage = (
                    group['roberta_pos'].sum() / row_total) * 100
                neutral_percentage = (
                    group['roberta_neu'].sum() / row_total) * 100
                negative_percentage = (
                    group['roberta_neg'].sum() / row_total) * 100

                rounded_positive = round(positive_percentage, 1)
                rounded_neutral = round(neutral_percentage, 1)
                rounded_negative = round(negative_percentage, 1)

                data.append({
                    "_id": ObjectId,
                    "Positive (%)": rounded_positive,
                    "Neutral (%)": rounded_neutral,
                    "Negative (%)": rounded_negative
                })
        df_table = pd.DataFrame(data)
    average_values = df_table.mean(numeric_only=True)
    average_negative = df_table["Negative (%)"].mean()
    average_neutral = df_table["Neutral (%)"].mean()
    average_positive = df_table["Positive (%)"].mean()
    print("Average Negative Percentage:", average_negative)
    print("Average Neutral Percentage:", average_neutral)
    print("Average Positive Percentage:", average_positive)

    return average_positive, average_negative, average_neutral

    print("yeta aaipuge ma")
    #  usage:

    #  collection_name = 'Pixel 7a - 128GB - Charcoal Pixel Buds A-Series - Charcoal'
    #  collection = db[collection_name]
    #  avg_negative, avg_neutral, avg_positive = process_nlp_collection(collection)
    #  print("Average Negative Percentage:", avg_negative)
    #  print("Average Neutral Percentage:", avg_neutral)
    #  print("Average Positive Percentage:", avg_positive)