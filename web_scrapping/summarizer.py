from transformers import pipeline
from database import get_database
reviews_arr = []
db = get_database()
keyword = "Apple watch SE 2"
cursor = db[keyword].find({})
for doc in cursor:
    reviews_arr.append(doc)

# print(reviews_arr)
overall = ""
print(reviews_arr[1]['Review'])
i = 0
while True:
    try:
        # print(reviews_arr[i]['Review'])
        overall = overall + reviews_arr[i]['Review']
        i = i + 1
    except:
        break
# print(overall)
summarizer = pipeline('summarization')

summary = summarizer(overall, max_length = 80, min_length = 30, do_sample = False)
print(summary[0]['summary_text'])