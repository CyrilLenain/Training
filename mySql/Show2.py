import pandas as pd
from sqlalchemy import create_engine

# Configuration de la connexion MySQL avec SQLAlchemy
db_config = {
    'user': 'root',                # Remplacez par votre nom d'utilisateur MySQL
    'password': '4253', # Remplacez par votre mot de passe MySQL
    'host': 'localhost',           # Hôte MySQL
    'database': 'bibliotheque'     # Nom de la base de données
}

# Création de l'URL de connexion en utilisant pymysql
db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"

# Création du moteur de connexion SQLAlchemy
engine = create_engine(db_url)

# Exécution de la requête SQL avec pandas
query = "SELECT * FROM Livres;"  # Exemple pour la table `Livres`
df = pd.read_sql(query, engine)

# Affichage des données de la table
print("\nTable 'livres' dans la base de données 'bibliotheque':")
print(df)

