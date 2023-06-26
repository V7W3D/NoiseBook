SELECT u.Nom, c.Prix, l.Adresse
FROM Utilisateur u
JOIN Concert c ON u.ID_utilisateur = c.ID_utilisateur
JOIN Lieu l ON c.ID_lieu = l.ID_lieu;


SELECT u.Nom, a.Commentaire
FROM Utilisateur u
LEFT JOIN Avis a ON u.ID_utilisateur = a.ID_utilisateur;


SELECT ID_utilisateur, COUNT(*) OVER(PARTITION BY ID_utilisateur) as Total_Interesse
FROM interesse_participe
WHERE participe = FALSE AND interesse = TRUE;


SELECT AVG(MaxPrice) as AverageOfMaxPrice
FROM (
    SELECT MAX(Prix) as MaxPrice
    FROM Concert
    GROUP BY ID_utilisateur
);


SELECT u.Nom
FROM Utilisateur u
WHERE NOT EXISTS (
    SELECT 1
    FROM Concert c
    WHERE c.ID_utilisateur = u.ID_utilisateur
    AND NOT EXISTS (
        SELECT 1
        FROM Avis a
        WHERE a.ID_utilisateur = u.ID_utilisateur
        AND a.ID_morceau = c.ID_Concert
    )
);

SELECT u.Nom, COUNT(*) as Number_of_Followers
FROM Utilisateur u
JOIN Suivre s ON u.ID_utilisateur = s.ID_utilisateur_1
GROUP BY u.Nom;


WITH RECURSIVE user_chain(ID_utilisateur, Nom, Email, depth, path) AS (
  SELECT u.ID_utilisateur, u.Nom, u.Email, 1, ARRAY[u.ID_utilisateur]
  FROM Utilisateur u
  WHERE u.ID_utilisateur = 1

  UNION ALL

  SELECT u.ID_utilisateur, u.Nom, u.Email, uc.depth + 1, path || u.ID_utilisateur
  FROM Utilisateur u
  JOIN Suivre s ON u.ID_utilisateur = s.ID_utilisateur_1
  JOIN user_chain uc ON s.ID_utilisateur = uc.ID_utilisateur
  WHERE NOT u.ID_utilisateur = ANY(uc.path)
)
SELECT * FROM user_chain ORDER BY depth;


SELECT u.Nom, u.Email, (SELECT COUNT(*) FROM publication p WHERE p.ID_publication = pub.ID_publication) AS Nombre_publications
FROM Utilisateur u, 
     (SELECT ID_utilisateur, ID_publication FROM publier) AS pub
WHERE u.ID_utilisateur = pub.ID_utilisateur;


SELECT u.Nom, u.Email 
FROM Utilisateur u 
WHERE u.ID_utilisateur IN (
    SELECT a.ID_utilisateur 
    FROM a_ecrit a
);