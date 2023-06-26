DROP TABLE IF EXISTS Avis_Tag;
DROP TABLE IF EXISTS Appartenir;
DROP TABLE IF EXISTS Ami;
DROP TABLE IF EXISTS Suivre;
DROP TABLE IF EXISTS interesse_participe;
DROP TABLE IF EXISTS tag_lieu;
DROP TABLE IF EXISTS tag_concert;
DROP TABLE IF EXISTS tag_playliste;
DROP TABLE IF EXISTS publier;
DROP TABLE IF EXISTS avis_concert;
DROP TABLE IF EXISTS avis_publication;
DROP TABLE IF EXISTS liker;
DROP TABLE IF EXISTS a_ecrit;
DROP TABLE IF EXISTS membre_du_groupe;
DROP TABLE IF EXISTS Avis;
DROP TABLE IF EXISTS Playlist;
DROP TABLE IF EXISTS Concert;
DROP TABLE IF EXISTS concert_fini;
DROP TABLE IF EXISTS concert_a_venir;
DROP TABLE IF EXISTS media;
DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS GenreMusical;
DROP TABLE IF EXISTS Tag;
DROP TABLE IF EXISTS Morceau;
DROP TABLE IF EXISTS Lieu;
DROP TABLE IF EXISTS SalleConcert;
DROP TABLE IF EXISTS Association;
DROP TABLE IF EXISTS Personne;
DROP TABLE IF EXISTS Groupe;
DROP TABLE IF EXISTS Utilisateur;

CREATE TABLE Utilisateur(
   ID_utilisateur INT,
   Nom VARCHAR(20) NOT NULL,
   Email VARCHAR(30) NOT NULL,
   PRIMARY KEY(ID_utilisateur),
   UNIQUE(Email)
);

CREATE TABLE Groupe(
   ID_utilisateur INT,
   Description VARCHAR(200),
   PRIMARY KEY(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Personne(
   ID_utilisateur INT,
   Prenom VARCHAR(20) NOT NULL,
   PRIMARY KEY(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Association(
   ID_utilisateur INT,
   Description VARCHAR(50),
   PRIMARY KEY(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE SalleConcert(
   ID_utilisateur INT,
   Adresse VARCHAR(100),
   PRIMARY KEY(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Lieu(
   ID_lieu INT,
   Adresse VARCHAR(100),
   PRIMARY KEY(ID_lieu)
);

CREATE TABLE Morceau(
   ID_morceau INT,
   Nom VARCHAR(20),
   PRIMARY KEY(ID_morceau)
);

CREATE TABLE Playlist(
   ID_playlist INT,
   Nom VARCHAR(20),
   ID_utilisateur INT,
   PRIMARY KEY(ID_playlist),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Avis(
   ID_avis INT,
   Note INT,
   Commentaire VARCHAR(200),
   ID_morceau INT NOT NULL,
   ID_utilisateur INT NOT NULL,
   ID_lieu INT NOT NULL,
   PRIMARY KEY(ID_avis),
   FOREIGN KEY(ID_morceau) REFERENCES Morceau(ID_morceau),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   FOREIGN KEY(ID_lieu) REFERENCES Lieu(ID_lieu)

);

CREATE TABLE Tag(
   ID_tag VARCHAR(50),
   Nom VARCHAR(50),
   PRIMARY KEY(ID_tag)
);

CREATE TABLE GenreMusical(
   ID_tag_1 VARCHAR(50),
   Nom VARCHAR(50),
   ID_tag VARCHAR(50),
   PRIMARY KEY(ID_tag_1),
   FOREIGN KEY(ID_tag_1) REFERENCES Tag(ID_tag),
   FOREIGN KEY(ID_tag) REFERENCES GenreMusical(ID_tag_1)
);

CREATE TABLE Concert(
   ID_Concert INT,
   Prix REAL,
   Nb_places INT,
   date_concert DATETIME,
   ID_lieu INT NOT NULL,
   ID_utilisateur INT NOT NULL,
   PRIMARY KEY(ID_Concert),
   FOREIGN KEY(ID_lieu) REFERENCES Lieu(ID_lieu),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   CHECK (Note >= 0 AND Note <= 5),
   CHECK (Nb_places > 0)
);

CREATE TABLE concert_fini(
   ID_Concert INT,
   nb_participant INT,
   PRIMARY KEY(ID_Concert),
   FOREIGN KEY(ID_Concert) REFERENCES Concert(ID_Concert)
);

CREATE TABLE concert_a_venir(
   ID_Concert INT,
   PRIMARY KEY(ID_Concert),
   FOREIGN KEY(ID_Concert) REFERENCES Concert(ID_Concert)
);

CREATE TABLE media(
   ID_media VARCHAR(50),
   ID_Concert INT,
   PRIMARY KEY(ID_media),
   FOREIGN KEY(ID_Concert) REFERENCES concert_fini(ID_Concert)
);

CREATE TABLE publication(
   ID_publication INT,
   contenu VARCHAR(255),
   ID_media VARCHAR(50),
   PRIMARY KEY(ID_publication),
   UNIQUE(ID_media),
   FOREIGN KEY(ID_media) REFERENCES media(ID_media)
);

CREATE TABLE Suivre(
   ID_utilisateur INT,
   ID_utilisateur_1 INT,
   PRIMARY KEY(ID_utilisateur, ID_utilisateur_1),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur_1) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Ami(
   ID_utilisateur INT,
   ID_utilisateur_1 INT,
   PRIMARY KEY(ID_utilisateur, ID_utilisateur_1),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur_1) REFERENCES Utilisateur(ID_utilisateur)
);

CREATE TABLE Appartenir(
   ID_morceau INT,
   ID_playlist INT,
   PRIMARY KEY(ID_morceau, ID_playlist),
   FOREIGN KEY(ID_morceau) REFERENCES Morceau(ID_morceau),
   FOREIGN KEY(ID_playlist) REFERENCES Playlist(ID_playlist)
);

CREATE TABLE Avis_Tag(
   ID_avis INT,
   ID_tag VARCHAR(50),
   PRIMARY KEY(ID_avis, ID_tag),
   FOREIGN KEY(ID_avis) REFERENCES Avis(ID_avis),
   FOREIGN KEY(ID_tag) REFERENCES Tag(ID_tag)
);

CREATE TABLE interesse_participe(
   ID_utilisateur INT,
   ID_Concert INT,
   participe BOOLEAN,
   interesse BOOLEAN,
   PRIMARY KEY(ID_utilisateur, ID_Concert),
   FOREIGN KEY(ID_utilisateur) REFERENCES Personne(ID_utilisateur),
   FOREIGN KEY(ID_Concert) REFERENCES Concert(ID_Concert),
   CHECK(participe = FALSE OR interesse = FLASE)
);

CREATE TABLE tag_lieu(
   ID_lieu INT,
   ID_tag VARCHAR(50),
   PRIMARY KEY(ID_lieu, ID_tag),
   FOREIGN KEY(ID_lieu) REFERENCES Lieu(ID_lieu),
   FOREIGN KEY(ID_tag) REFERENCES Tag(ID_tag)
);

CREATE TABLE tag_concert(
   ID_Concert INT,
   ID_tag VARCHAR(50),
   PRIMARY KEY(ID_Concert, ID_tag),
   FOREIGN KEY(ID_Concert) REFERENCES Concert(ID_Concert),
   FOREIGN KEY(ID_tag) REFERENCES Tag(ID_tag)
);

CREATE TABLE tag_playliste(
   ID_playlist INT,
   ID_tag VARCHAR(50),
   PRIMARY KEY(ID_playlist, ID_tag),
   FOREIGN KEY(ID_playlist) REFERENCES Playlist(ID_playlist),
   FOREIGN KEY(ID_tag) REFERENCES Tag(ID_tag)
);

CREATE TABLE publier(
   ID_utilisateur INT,
   ID_publication INT,
   PRIMARY KEY(ID_utilisateur, ID_publication),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   FOREIGN KEY(ID_publication) REFERENCES publication(ID_publication)
);

CREATE TABLE avis_concert(
   ID_avis INT,
   ID_Concert INT,
   PRIMARY KEY(ID_avis, ID_Concert),
   FOREIGN KEY(ID_avis) REFERENCES Avis(ID_avis),
   FOREIGN KEY(ID_Concert) REFERENCES concert_fini(ID_Concert)
);

CREATE TABLE avis_publication(
   ID_avis INT,
   ID_publication INT,
   PRIMARY KEY(ID_avis, ID_publication),
   FOREIGN KEY(ID_avis) REFERENCES Avis(ID_avis),
   FOREIGN KEY(ID_publication) REFERENCES publication(ID_publication)
);

CREATE TABLE liker(
   ID_utilisateur INT,
   ID_publication INT,
   PRIMARY KEY(ID_utilisateur, ID_publication),
   FOREIGN KEY(ID_utilisateur) REFERENCES Utilisateur(ID_utilisateur),
   FOREIGN KEY(ID_publication) REFERENCES publication(ID_publication)
);

CREATE TABLE a_ecrit(
   ID_utilisateur INT,
   ID_morceau INT,
   PRIMARY KEY(ID_utilisateur, ID_morceau),
   FOREIGN KEY(ID_utilisateur) REFERENCES Personne(ID_utilisateur),
   FOREIGN KEY(ID_morceau) REFERENCES Morceau(ID_morceau)
);

CREATE TABLE membre_du_groupe(
   ID_utilisateur INT,
   ID_utilisateur_1 INT,
   PRIMARY KEY(ID_utilisateur, ID_utilisateur_1),
   FOREIGN KEY(ID_utilisateur) REFERENCES Groupe(ID_utilisateur),
   FOREIGN KEY(ID_utilisateur_1) REFERENCES Personne(ID_utilisateur)
);
