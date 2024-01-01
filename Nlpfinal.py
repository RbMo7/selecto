import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import nltk
nltk.download('punkt')


!pip install pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://selecto:DmdSvpAnRnudk1Zj@reviews-list.q56a6p2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['Reviews']  # Replace 'your_database' with your database name

# List collections within the database
collection_names = db.list_collection_names()

# Display the collection names
print("Collections in the database:")
for name in collection_names:
    print(name)

db = client['Reviews']
collection = db['Apple watch SE 2']

# Retrieve the first 20 documents from the collection
cursor = collection.find().limit(20)

# Display the fetched documents
for document in cursor:
    print(document)

# Retrieve the data from the collection
data = list(collection.find())

# Create a DataFrame for tabular representation
df = pd.DataFrame(data)

# Display the data in a table
df.head()



example = df['Review'][2]
print(example)

tokens=nltk.word_tokenize(example)
tokens[:100000]

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

tagged = nltk.pos_tag(tokens)
tagged [:100000]

entities = nltk.chunk.ne_chunk(tagged)
entities.pprint()

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
sia = SentimentIntensityAnalyzer()

sia.polarity_scores('I am so happy!')

sia.polarity_scores(example)

res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Review']
    myid = row['_id']

    # Check if the 'text' variable is a string
    if isinstance(text, str):
        res[myid] = sia.polarity_scores(text)
    else:
        # Handle other data types (e.g., float) as needed
        print(f"Skipping row with non-string data at index {i}")

# Print the results
print(res)


df['Review'] = df['Review'].astype(str) #Converting non string data
res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Review']
    myid = row['_id']

    # Check if the 'text' variable is a string
    if isinstance(text, str):
        res[myid] = sia.polarity_scores(text)
    else:
        # Handle other data types (e.g., float) as needed
        print(f"Skipping row with non-string data at index {i}")

# Print the results
print(res)



vaders=pd.DataFrame(res).T
vaders=vaders.reset_index().rename(columns={'index':'_id'})
vaders= vaders.merge(df,how = 'left')

grouped = vaders.groupby('_id').sum()
data = []

for product_id, row in grouped.iterrows():
    row_total = row['pos'] + row['neu'] + row['neg']
    if row_total > 0:
        positive_percentage = (row['pos'] / row_total) * 100
        neutral_percentage = (row['neu'] / row_total) * 100
        negative_percentage = (row['neg'] / row_total) * 100

        rounded_positive = round(positive_percentage, 1)
        rounded_neutral = round(neutral_percentage, 1)
        rounded_negative = round(negative_percentage, 1)

        data.append({
            "Product ID": product_id,
            "Positive (%)": rounded_positive,
            "Neutral (%)": rounded_neutral,
            "Negative (%)": rounded_negative
        })

# Create a DataFrame from the data
df_table = pd.DataFrame(data)

# Display the table
print(df_table)

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer= AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

#Vaders resultss on example
print(example)
sia.polarity_scores(example)

# Run for Roberta
encoded_text = tokenizer(example, return_tensors='pt')
output = model(**encoded_text)
scores = output[0][0].detach().numpy()
scores = softmax(scores)
scores_dict= {
    'roberta_neg' : scores[0],
    'roberta_neu' : scores[1],
    'roberta_pos' : scores[2]
}
print(scores_dict)

def polarity_scores_roberta(example) :
  encoded_text = tokenizer(example, return_tensors='pt')
  output = model(**encoded_text)
  scores = output[0][0].detach().numpy()
  scores = softmax(scores)
  scores_dict= {
    'roberta_neg' : scores[0],
    'roberta_neu' : scores[1],
    'roberta_pos' : scores[2]
  }
  return scores_dict





df['Review'] = df['Review'].astype(str) #Converting non string data
res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Review']
    myid = row['_id']

    # Check if the 'text' variable is a string
    if isinstance(text, str):
        res[myid] =  polarity_scores_roberta(text)
    else:
        # Handle other data types (e.g., float) as needed
        print(f"Skipping row with non-string data at index {i}")

# Print the results
print(res)

roberta=pd.DataFrame(res).T
roberta=roberta.reset_index().rename(columns={'index':'_id'})
roberta= roberta.merge(df,how = 'left')


data = []

for ObjectId, row in grouped.iterrows():
    row_total = row['roberta_pos'] + row['roberta_neu'] + row['roberta_neg']

    if row_total > 0:
        positive_percentage = (row['roberta_pos'] / row_total) * 100
        neutral_percentage = (row['roberta_neu'] / row_total) * 100
        negative_percentage = (row['roberta_neg'] / row_total) * 100

        rounded_positive = round(positive_percentage, 1)
        rounded_neutral = round(neutral_percentage, 1)
        rounded_negative = round(negative_percentage, 1)

        data.append({
            "Product ID": ObjectId,
            "Positive (%)": rounded_positive,
            "Neutral (%)": rounded_neutral,
            "Negative (%)": rounded_negative
        })

# Create a DataFrame from the data
df_table = pd.DataFrame(data)

# Display the table
print(df_table)


from transformers import pipeline

import textwrap

reviews = df['Review'].tolist()

# Combine all reviews into a single text
combined_text = ' '.join(reviews)

# Wrap the text to limit the length of each sequence
wrapped_text = textwrap.fill(combined_text, width=1020)  # Adjust the width as needed

# Load pre-trained BART model for abstractive summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

# Generate abstractive summary for each sequence
abstractive_summary = []
for chunk in wrapped_text.split('\n'):
    summary_chunk = summarizer(chunk, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    abstractive_summary.append(summary_chunk[0]['summary_text'])

# Combine the summaries
final_summary = ' '.join(abstractive_summary)

# Print the final abstractive summary
print(final_summary)

nltk.download('punkt')

def cut_text_into_sentences(text, num_sentences=5):
    sentences = nltk.sent_tokenize(text)
    return ' '.join(sentences[:num_sentences])

# Cut the summary to the desired number of sentences
cut_summary = cut_text_into_sentences(final_summary, num_sentences=3)  # Adjust num_sentences as needed

# Print the shortened summary
print(cut_summary)


