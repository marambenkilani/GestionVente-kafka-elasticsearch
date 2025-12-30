
# ======================================================
# 📊 Big Data Pipeline – Analyse des Ventes E-commerce
# ======================================================

# 🧠 Description du projet
 Ce projet met en place un pipeline Big Data scalable pour analyser les ventes e-commerce.
 Les données sont ingérées depuis des fichiers CSV, traitées en temps réel et visualisées via des dashboards.

# ------------------------------------------------------
#  Objectifs
 - Gérer de grands volumes de données de ventes
 - Traiter les données en temps réel
 - Nettoyer et transformer les données
 - Stocker efficacement les données
 - Fournir des tableaux de bord décisionnels

# ------------------------------------------------------
#  Architecture du projet
 CSV → Python → Kafka → Logstash → Elasticsearch → Kibana

# ------------------------------------------------------
#  Technologies utilisées
 - Python : ingestion, nettoyage et transformation
 - Apache Kafka : streaming des données
 - Logstash : traitement et indexation
 - Elasticsearch : stockage et recherche
 - Kibana : visualisation et dashboards
 - Docker & Docker Compose : orchestration des services

# ------------------------------------------------------
#  Structure du projet

 bigdataproject/
 ├── data/
 │   └── online_retail.csv
 ├── producer/
 │   └── send_to_kafka.py
 ├── logstash/
 │   └── logstash.conf
 ├── docker-compose.yml
 └── README.md

# ------------------------------------------------------
#  Démarrage rapide

 1️⃣ Lancer tous les services :
 docker-compose up -d

 2️⃣ Envoyer les données vers Kafka :
 python producer/send_to_kafka.py

 3️⃣ Accéder aux interfaces :
 - Kafka UI : http://localhost:8080
 - Kibana  : http://localhost:5601
 - Elasticsearch : http://localhost:9200

# ------------------------------------------------------
#  KPI analysés
 - Chiffre d’affaires total
 - Nombre de ventes
 - Ventes par pays
 - Ventes par période (jour / mois / année)
 - Produits les plus vendus
 - Taux d’annulation

# ------------------------------------------------------
#  Scalabilité
 - Kafka permet le traitement distribué des flux
 - Elasticsearch supporte de grands volumes de données
 - Docker facilite le déploiement et l’extension du système

# ------------------------------------------------------
#  Visualisation
 Les données sont visualisées dans Kibana à travers des tableaux de bord interactifs pour l’aide à la décision.

# ------------------------------------------------------
# 👩‍💻 Auteur
# Maram Benkilani
# Projet académique – Big Data & Business Intelligence

# ------------------------------------------------------
# 📌 Mots-clés
 Big Data, Kafka, ELK Stack, Docker, E-commerce, Data Pipeline, Data Analytics
