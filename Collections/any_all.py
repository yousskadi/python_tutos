# LES COLLECTIONS: LISTES /TUPLES
## Any et ALL
# Any : Quelconque / n'importe quel - Si un éléments est valide == True
# All : Tout / Toutes - Si tous éléments sont valide == True sinon False
##

#         0         1          2        3         4         5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Claire"]

##Methode Classique
# found = False
# for nom in noms:
#     if "z" in nom.lower():
#         found = True
#         break
# if found:
#     print("Trouvé")
# else:
#     print("Non trouvé")



##Methode avec Any et ALL
## si la 1 ere lettre de l'élément nom contient la lettre cité dans any
## renvoie True si au moins un élément est valide
# print(any([nom[0] == "C" for nom in noms]))
# print(any([nom[0] == "Z" for nom in noms]))

## Methode avec le comprehension de liste
noms_avec_z = any([True if "z" in nom.lower() else False for nom in noms])
if noms_avec_z:
    print("Trouvé")
else:
    print("Non trouvé")
