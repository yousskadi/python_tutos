# LES COLLECTIONS: LISTES /TUPLES
## index, find, count

#         0         1          2        3         4         5
noms = ["Jean", "Youssef", "Yasmina", "Adam", "Mohamed", "Adam"]

# print(noms.index("Jean")) ## index() renvoie l'index de l'élément
# print(noms.index("Adam"))

# element_cherche = "toto"
# if element_cherche in noms:
#     print(noms.index(element_cherche))
#     print("Trouvé")

# else:
#     print("Non trouvé")

# NB: index vous donne toujours la valeur du premier éléments qu'il aura trouvé
# on pourrait lui dire de continuer à chercher à partir de l'index 2 par exemple
#print(noms.index("Adam", 2))

## count: compte le nombre d'occurence d'un élément
#print(noms.count("Adam"))

# element_cherche = "Adam"
# nb_occurences = noms.count(element_cherche)
# print("nb_occurences",  nb_occurences)
# if nb_occurences > 0:
#     index_occurence = 0
#     for i in range(nb_occurences):
#         index_occurence = noms.index(element_cherche, index_occurence)
#         print(element_cherche, "trouvé à", index_occurence)
#         index_occurence += 1
# else:
#     print("Non trouvé")

## Find fonctionne sur des Str, non sur des Collections
#print(noms.find("Adam"))  ## ce ne fonctionne pas
### si pas trouvée renvoie -1
a = "Youssef-kadi-Yasmina"
i = a.find("Yasmina")
print(i)