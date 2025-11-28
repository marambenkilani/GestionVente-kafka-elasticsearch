from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    hosts=["http://localhost:9200"],
    request_timeout=30,
)

index_name = "ventes_ecommerce1"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

print("Consumer Kafka → Elasticsearch démarré...")

consumer = KafkaConsumer(
    "ventes_ecommerce",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    print(f"Message reçu : {message.value}")

    # INDEXATION DIRECTE DU DICT JSON
    es.index(index=index_name, document=message.value)

    print("→ Document indexé dans ES")
