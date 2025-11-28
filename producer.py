import json
import uuid
import pandas as pd
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

# ------------------------------
# 1) Création du topic (si besoin)
# ------------------------------

admin = KafkaAdminClient(bootstrap_servers="localhost:9092")

try:
    admin.create_topics([
        NewTopic(name="ventes_ecommerce1", num_partitions=1, replication_factor=1)
    ])
    print("✅ Topic 'ventes_ecommerce1' créé")
except Exception:
    print("ℹ️ Topic déjà existant")

print("Topics existants :", admin.list_topics())

# ------------------------------
# 2) Préparation du dataset
# ------------------------------

df = pd.read_csv("C:\\bigdataproject\\data\\data1.csv", sep=";", encoding="latin1")

df = df.dropna(subset=["CustomerID"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors='coerce')
df["Description"] = df["Description"].str.strip()

df["MontantTotal"] = df["Quantity"] * df["UnitPrice"]
df["Annulation"] = df["InvoiceNo"].astype(str).str.startswith("C")
df["Jour"] = df["InvoiceDate"].dt.day
df["Mois"] = df["InvoiceDate"].dt.month
df["Annee"] = df["InvoiceDate"].dt.year
df["Heure"] = df["InvoiceDate"].dt.hour
df["Country"] = df["Country"].replace({"United Kingdom": "UK"})
df["uuid"] = [str(uuid.uuid4()) for _ in range(len(df))]

# ------------------------------
# 3) Envoi vers Kafka
# ------------------------------

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
)

for _, row in df.iterrows():
    producer.send("ventes_ecommerce1", row.to_dict())

producer.flush()

print("🚀 Toutes les données ont été envoyées à Kafka !")
