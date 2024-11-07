import pandas as pd
from sqlalchemy import create_engine

# Configuration de la connexion
user = "root"  # Nom de l'utilisateur MySQL
password = "4253"  # Remplacez par votre mot de passe
host = "localhost"  # Adresse du serveur MySQL
database = "bibliotheque"  # Nom de la base de données

# Création de l'engine SQLAlchemy pour MySQL avec pymysql
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# Essayez de lire les données de la table 'livres'
try:
    # Utiliser la requête SQL directement
    query = "SELECT * FROM Livres"
    df = pd.read_sql_query(query, con=engine)  # Remplacez 'read_sql' par 'read_sql_query'
    print(df)
except Exception as e:
    print(f"Erreur lors de la récupération des données : {e}")
finally:
    engine.dispose()  # Fermer la connexion proprement

