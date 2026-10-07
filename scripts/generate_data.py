from faker import Faker
import random
import datetime
import pandas as pd

fake = Faker()

NUM_ORDERS = 1000
cat = ["Électronique", "Vêtements", "Maison", "Livres"]
statut = ["Livré", "En cours", "Annulé"]

orders = []
for i in range(NUM_ORDERS) : 
    s = random.randint(0,2)
    p = random.randint(0,3)
    order = {
        "order_id" : i+1,
        "customer_id" : random.randint(1000, 1050),
        "order_date" : fake.date_between(start_date ='-1y', end_date='today'),
        "product_category" : cat[p],
        "quantity" : random.randint(1,5),
        "unit_price" : round(random.uniform(10.0, 200.0), 2),
        "status" : statut[s],
    }
    orders.append(order)
df = pd.DataFrame(orders)
df.to_csv("data/raw_orders.csv", index=False)