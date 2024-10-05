import pandas as pd
from sklearn.cluster import KMeans
from pymongo import MongoClient
import json

# Load customer data from JSON file
with open('customer_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Perform K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(df[['age', 'income', 'spending_score']])
df['cluster'] = kmeans.labels_

# Convert to JSON format
json_data = df.to_json(orient='records')

# Save JSON data to a file
with open('segmented_customer_data.json', 'w') as f:
    f.write(json_data)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://akanksha-priya:Akanksha2005@project.oqccibb.mongodb.net/")
db = client['customer_segmentation']
collection = db['customers']

# Insert data into MongoDB
collection.insert_many(json.loads(json_data))

print("Data inserted into MongoDB Atlas")
