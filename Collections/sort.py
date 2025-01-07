# LES COLLECTIONS: LISTES /TUPLES
## Tris: Sort /Sorted
## tri par ordre alphabetique STR
## Tri par ordre croissant INT


#         0         1          2        3
noms = ["Jean", "Youssef", "Yasmina", "Adam"]

#noms.sort()   ## opération "inplace" modifie la liste en mémoire
#noms.sort(reverse=True)  ## on trie dans l'autre sens
#noms.sort(key=lambda nom : len(nom)) ## tri personalisé
noms.sort(key=len)
## sorted() est une fonction qui prend une Collection et renvoie en sortie une nouvelle liste
#noms_tries = sorted(noms)  ## création une nouvelle liste
#noms_tries = sorted(noms, reverse=True) ## on trie dans l'autre sens
noms_tries = sorted(noms,key=len, reverse=True)
## .sort() et sorted() s'utilise de la même manière
print(noms)  #
print(noms_tries)