from pymongo import MongoClient

client = MongoClient("mongodb+srv://akanksha-priya:Akanksha2005@project.oqccibb.mongodb.net/")

db = client.get_database('Project')
collection = db['data']

from faker import Faker
import pandas as pd
import numpy as np
import json

fake = Faker()
data = []

for _ in range(100):
    customer = {
        'name': fake.name(),
        'age': np.random.randint(18, 70),
        'income': np.random.randint(20000, 150000),
        'spending_score': np.random.randint(1, 100)
    }
    data.append(customer)

df = pd.DataFrame(data)
df.to_csv('customer_data.csv', index=False)

# Convert to JSON and save
json_data = df.to_json(orient='records')
with open('customer_data.json', 'w') as f:
    f.write(json_data)

print("Data generated and saved to customer_data.csv and customer_data.json")
