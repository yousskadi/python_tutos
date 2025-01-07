# LES COLLECTIONS: LISTES /TUPLES
## swapper 2 éléments (échanger)


#         0         1          2        3         4
noms = ["Jean", "Youssef", "Yasmina", "Adam", "Mohamed"]

## 1 ere methode avec un variable intermédiaire
# t = noms[0]
# noms[0] = noms[4]
# noms[4] = t

## 1 ere methode sur une seule ligne directement vers l'échange
#                   Mohamed   Jean
noms[1], noms[2] = noms[2], noms[1]
print(noms)