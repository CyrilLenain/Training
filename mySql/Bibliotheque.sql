
CREATE DATABASE bibliotheque;
USE bibliotheque;

-- Supprimer les tables existantes
DROP TABLE IF EXISTS Emprunts;
DROP TABLE IF EXISTS Livres;
DROP TABLE IF EXISTS Auteurs;

-- Créer les tables
CREATE TABLE Auteurs (
  auteur_id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  nationalite VARCHAR(50)
);

CREATE TABLE Livres (
  livre_id INT AUTO_INCREMENT PRIMARY KEY,
  titre VARCHAR(100),
  genre VARCHAR(50),
  auteur_id INT,
  FOREIGN KEY (auteur_id) REFERENCES Auteurs(auteur_id)
);

CREATE TABLE Emprunts (
  emprunt_id INT AUTO_INCREMENT PRIMARY KEY,
  livre_id INT,
  date_emprunt DATE,
  date_retour DATE,
  FOREIGN KEY (livre_id) REFERENCES Livres(livre_id)
);

-- Insérer des données
INSERT INTO Auteurs (nom, nationalite) VALUES ('Gabriel Garcia Marquez', 'Colombienne');
INSERT INTO Auteurs (nom, nationalite) VALUES ('Chinua Achebe', 'Nigérienne');

INSERT INTO Livres (titre, genre, auteur_id) VALUES ('Cent ans de solitude', 'Fiction', 1);
INSERT INTO Livres (titre, genre, auteur_id) VALUES ('Things Fall Apart', 'Fiction', 2);

INSERT INTO Emprunts (livre_id, date_emprunt, date_retour) VALUES (1, '2024-01-01', '2024-01-15');
INSERT INTO Emprunts (livre_id, date_emprunt, date_retour) VALUES (2, '2024-01-02', NULL);