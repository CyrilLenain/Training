import pandas as pd
import mysql.connector as mysql

# Configuration de la connexion MySQL
db_config = {
    'host': 'localhost',       # Remplacez par votre hôte
    'user': 'root',            # Remplacez par votre nom d'utilisateur MySQL
    'password': '4253',  # Remplacez par votre mot de passe MySQL
    'database': 'bibliotheque' # Nom de la base de données
}

# Connexion à la base de données
try:
    conn = mysql.connect(**db_config)
    print("Connexion réussie à la base de données")

    # Lecture de la table avec pandas
    query = "SELECT * FROM Livres;"  # Exemple pour la table `livres` dans `bibliotheque`
    df = pd.read_sql(query, conn)

    # Affichage du tableau
    print("\nTable 'livres' dans la base de données 'bibliotheque':")
    print(df)

except mysql.Error as err:
    print(f"Erreur: {err}")

finally:
    # Fermeture de la connexion
    if conn.is_connected():
        conn.close()
        print("Connexion à la base de données fermée.")

