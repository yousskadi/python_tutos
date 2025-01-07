# LES COLLECTIONS: LISTES /TUPLES
## les comprehension de listes


#         0         1          2        3         4         5
noms = ["Jean", "Youssef", "Yasmina", "Adam", "Mohamed", "Adam"]

## 1 ere methode
# longueur_noms = []
# for nom in noms:
#     longueur_noms.append(len(nom))
## 2 ème methode
# longueur_noms = [len(nom) for nom in noms]
## 3 ème methode
# ajout d'une condition ici on ajoute la longueur si > 5
#longueur_noms = [len(nom) for nom in noms if len(nom) > 5]
## 4 ème methode
# longueur_noms = [nom if len(nom) > 5 else 0 for nom in noms]
# ## 5 ème methode
longueur_noms = [len(nom) if len(nom) > 5 else 0 for nom in noms]
## 6 ème methode
#longueur_noms = [len(nom) if nom != "Adam" else 0 for nom in noms]
## 7 ème methode
## si le nom contient un "e"
#nom_avec_e = [nom for nom in noms if "i" in nom]
# exemple avec des opérations
## i//2 opération entière pas de virgule
#a = [i for i in range(11) if (i//2)*2 == i]
## b - Mettre True si Pair
#b= [True if (i//2)*2 ==i else False for i in range(11)]
## c - créer une liste de Tuples
c= [(i, True if (i//2)*2 ==i else False) for i in range(11)]
print(c)