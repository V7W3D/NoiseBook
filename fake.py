import csv
import random
from faker import Faker

fake = Faker()

# Constants
N = 50

# Store IDs
utilisateur_ids = []
groupe_ids = []
personne_ids = []
association_ids = []
salle_concert_ids = []
lieu_ids = []
morceau_ids = []
playlist_ids = []
tag_ids = []
avis_ids = []
genre_musical_ids = []
concert_ids = []
concert_fini_ids = []
concert_a_venir_ids = []
media_ids = []
publication_ids = []


# 1. Utilisateur
with open('Utilisateur.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'Nom', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1, N + 1):
        ID_utilisateur = i
        utilisateur_ids.append(ID_utilisateur)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'Nom': fake.name(),
            'Email': fake.email(),
        })


# 3. Personne
with open('Personne.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'Prénom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        personne_ids.append(i)
        row = {
            'ID_utilisateur': i,
            'Prénom': fake.first_name()
        }
        writer.writerow(row)

# 2. Groupe
with open('Groupe.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_groupe', 'Nom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1, N + 1):
        ID_groupe = i
        groupe_ids.append(ID_groupe)

        writer.writerow({
            'ID_groupe': ID_groupe,
            'Nom': fake.word(),
        })


# 4. Association
with open('Association.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        row = {
            'ID_utilisateur': i,
            'Description': fake.text(max_nb_chars=50)
        }
        writer.writerow(row)

# 5. SalleConcert
with open('SalleConcert.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'Adresse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        row = {
            'ID_utilisateur': i,
            'Adresse': fake.address()
        }
        writer.writerow(row)

# 6. Lieu
with open('Lieu.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_lieu', 'Adresse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        row = {
            'ID_lieu': i,
            'Adresse': fake.address()
        }
        writer.writerow(row)
        lieu_ids.append(i)  # save for future reference

# 7. Morceau
with open('Morceau.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_morceau', 'Nom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_morceau = i
        morceau_ids.append(ID_morceau)

        writer.writerow({
            'ID_morceau': ID_morceau,
            'Nom': fake.word(),
        })


# 8. Playlist
with open('Playlist.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_playlist', 'Nom', 'ID_utilisateur']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_playlist = i
        playlist_ids.append(ID_playlist)
        ID_utilisateur = random.choice(utilisateur_ids)

        writer.writerow({
            'ID_playlist': ID_playlist,
            'Nom': fake.word(),
            'ID_utilisateur': ID_utilisateur,
        })


# 9. Avis
with open('Avis.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_avis', 'Note', 'Commentaire', 'ID_morceau', 'ID_utilisateur', 'ID_lieu']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_avis = i
        avis_ids.append(ID_avis)
        ID_morceau = random.choice(morceau_ids)
        ID_utilisateur = random.choice(utilisateur_ids)
        ID_lieu = random.choice(lieu_ids)

        writer.writerow({
            'ID_avis': ID_avis,
            'Note': random.randint(0, 5),
            'Commentaire': fake.text(max_nb_chars=200),
            'ID_morceau': ID_morceau,
            'ID_utilisateur': ID_utilisateur,
            'ID_lieu': ID_lieu,
        })


# 10. Tag
with open('Tag.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_tag', 'Nom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_tag = i
        tag_ids.append(ID_tag)

        writer.writerow({
            'ID_tag': ID_tag,
            'Nom': fake.word(),
        })


# 11. GenreMusical
with open('GenreMusical.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_tag_1', 'Nom', 'ID_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_tag_1 = i
        genre_musical_ids.append(ID_tag_1)
        ID_tag = random.choice(tag_ids)

        writer.writerow({
            'ID_tag_1': ID_tag_1,
            'Nom': fake.word(),
            'ID_tag': ID_tag,
        })


# 12. Concert
with open('Concert.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_Concert', 'Prix', 'Nb_places', 'date_concert', 'ID_lieu', 'ID_utilisateur']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_Concert = i
        concert_ids.append(ID_Concert)
        ID_lieu = random.choice(lieu_ids)
        ID_utilisateur = random.choice(utilisateur_ids)

        writer.writerow({
            'ID_Concert': ID_Concert,
            'Prix': round(random.uniform(10, 100), 2),
            'Nb_places': random.randint(1, 100),
            'date_concert': fake.date_time_this_year(),
            'ID_lieu': ID_lieu,
            'ID_utilisateur': ID_utilisateur,
        })


# 13. concert_fini
with open('concert_fini.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_Concert', 'nb_participant']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_Concert = i
        concert_fini_ids.append(ID_Concert)

        writer.writerow({
            'ID_Concert': ID_Concert,
            'nb_participant': random.randint(1, 1000),
        })


# 14. concert_a_venir
with open('concert_a_venir.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_Concert']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_Concert = i
        concert_a_venir_ids.append(ID_Concert)

        writer.writerow({
            'ID_Concert': ID_Concert,
        })


# 15. media
with open('media.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_media', 'ID_Concert']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_media = fake.uuid4()
        media_ids.append(ID_media)
        ID_Concert = random.choice(concert_fini_ids)

        writer.writerow({
            'ID_media': ID_media,
            'ID_Concert': ID_Concert,
        })


# 16. publication
with open('publication.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_publication', 'contenu', 'ID_media']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, N + 1):
        ID_publication = i
        publication_ids.append(ID_publication)
        ID_media = random.choice(media_ids)

        writer.writerow({
            'ID_publication': ID_publication,
            'contenu': fake.text(max_nb_chars=255),
            'ID_media': ID_media,
        })


# 17. Suivre
with open('Suivre.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_utilisateur_1']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        ID_utilisateur = i
        ID_utilisateur_1 = random.choice(utilisateur_ids)

        while ID_utilisateur == ID_utilisateur_1:
            ID_utilisateur_1 = random.choice(utilisateur_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_utilisateur_1': ID_utilisateur_1
        })


# 18. Ami
with open('Ami.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_utilisateur_1']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        ID_utilisateur = i
        ID_utilisateur_1 = random.choice(utilisateur_ids)

        while ID_utilisateur == ID_utilisateur_1:
            ID_utilisateur_1 = random.choice(utilisateur_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_utilisateur_1': ID_utilisateur_1
        })


# 19. Appartenir
with open('Appartenir.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_morceau', 'ID_playlist']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in morceau_ids:
        ID_morceau = i
        ID_playlist = random.choice(playlist_ids)

        writer.writerow({
            'ID_morceau': ID_morceau,
            'ID_playlist': ID_playlist,
        })


# 20. Avis_Tag
with open('Avis_Tag.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_avis', 'ID_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in avis_ids:
        ID_avis = i
        ID_tag = random.choice(tag_ids)

        writer.writerow({
            'ID_avis': ID_avis,
            'ID_tag': ID_tag,
        })


# 21. interesse_participe
with open('interesse_participe.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_Concert', 'participe', 'interesse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in personne_ids:
        ID_utilisateur = i
        ID_Concert = random.choice(concert_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_Concert': ID_Concert,
            'participe': random.choice([True, False]),
            'interesse': random.choice([True, False]),
        })


# 22. tag_lieu
with open('tag_lieu.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_lieu', 'ID_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in lieu_ids:
        ID_lieu = i
        ID_tag = random.choice(tag_ids)

        writer.writerow({
            'ID_lieu': ID_lieu,
            'ID_tag': ID_tag,
        })


# 23. tag_concert
with open('tag_concert.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_Concert', 'ID_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in concert_ids:
        ID_Concert = i
        ID_tag = random.choice(tag_ids)

        writer.writerow({
            'ID_Concert': ID_Concert,
            'ID_tag': ID_tag,
        })


# 24. tag_playliste
with open('tag_playliste.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_playlist', 'ID_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in playlist_ids:
        ID_playlist = i
        ID_tag = random.choice(tag_ids)

        writer.writerow({
            'ID_playlist': ID_playlist,
            'ID_tag': ID_tag,
        })


# 25. publier
with open('publier.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_publication']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        ID_utilisateur = i
        ID_publication = random.choice(publication_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_publication': ID_publication,
        })


# 26. avis_concert
with open('avis_concert.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_avis', 'ID_Concert']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in avis_ids:
        ID_avis = i
        ID_Concert = random.choice(concert_fini_ids)

        writer.writerow({
            'ID_avis': ID_avis,
            'ID_Concert': ID_Concert,
        })


# 27. avis_publication
with open('avis_publication.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_avis', 'ID_publication']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in avis_ids:
        ID_avis = i
        ID_publication = random.choice(publication_ids)

        writer.writerow({
            'ID_avis': ID_avis,
            'ID_publication': ID_publication,
        })


# 28. liker
with open('liker.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_publication']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in utilisateur_ids:
        ID_utilisateur = i
        ID_publication = random.choice(publication_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_publication': ID_publication,
        })


# 29. a_ecrit
with open('a_ecrit.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_morceau']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in personne_ids:
        ID_utilisateur = i
        ID_morceau = random.choice(morceau_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_morceau': ID_morceau,
        })


# 30. membre_du_groupe
with open('membre_du_groupe.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID_utilisateur', 'ID_utilisateur_1']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in groupe_ids:
        ID_utilisateur = i
        ID_utilisateur_1 = random.choice(personne_ids)

        writer.writerow({
            'ID_utilisateur': ID_utilisateur,
            'ID_utilisateur_1': ID_utilisateur_1
        })
