# LES COLLECTIONS: LISTES /TUPLES
## SLICES

#         0         1          2        3
noms = ["Jean", "Youssef", "Yasmina", "Adam"]

#slice_noms = noms
## slice_noms et noms pointe sur la même liste en mémoire donc toutes modifications de slice_noms ou noms modifie la liste
slice_noms = noms[:]
## ici on fait une copie de la liste mais ne pointe pas sur la même liste.
## donc toutes modifications de slice_noms ou noms ne modifie la liste
slice_noms[0] = "Mohamed"
noms[0] = "KADI"
#print(slice_noms)
## Résultats avec slice_noms = noms
# ['Mohamed', 'Youssef', 'Yasmina', 'Adam']
## Résultats avec slice_noms = noms[:]
#['Mohamed', 'Youssef', 'Yasmina', 'Adam']
#print(noms)
## Résultats avec slice_noms = noms
# ['Mohamed', 'Youssef', 'Yasmina', 'Adam']
## Résultats avec slice_noms = noms[:]
#['KADI', 'Youssef', 'Yasmina', 'Adam']
## NB: 2 résultats différents car ce sont 2  listes différentes


### Si on souhaite exclure le dernier éléments de la liste
#slice_noms = noms[:len(noms)-1]
## ou avec le -1
slice_noms = noms[:-1]
print(slice_noms)
