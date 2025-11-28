# send_to_kafka.py
import pandas as pd
from kafka import KafkaProducer
import json
import uuid

df = pd.read_csv(r"C:\bigdataproject\data\online_retail.csv", encoding="utf-8", sep='\t')  # ou sep=','

# Nettoyage
df = df.dropna(subset=["CustomerID"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True)  # dayfirst selon format
df["Description"] = df["Description"].str.strip()

# Transformations
df["MontantTotal"] = df["Quantity"] * df["UnitPrice"]
df["Annulation"] = df["InvoiceNo"].astype(str).str.startswith("C")
df["Jour"] = df["InvoiceDate"].dt.day
df["Mois"] = df["InvoiceDate"].dt.month
df["Annee"] = df["InvoiceDate"].dt.year
df["Heure"] = df["InvoiceDate"].dt.hour
df["Country"] = df["Country"].replace({"United Kingdom": "UK"})
df["uuid"] = [str(uuid.uuid4()) for _ in range(len(df))]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
)

for _, row in df.iterrows():
    producer.send("ventes_ecommerce", row.to_dict())

producer.flush()
print("🚀 Envoi terminé dans Kafka !")
