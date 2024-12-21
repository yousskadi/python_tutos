# LES COLLECTIONS: LISTES /TUPLES
## Append /Extend / += / Insert

noms = ["Jean", "Youssef", "Yasmina", "Adam"]


noms_supp = ["Toto", "Titi"]

#noms.append(noms_supp)
## Résultats
# ['Jean', 'Youssef', 'Yasmina', 'Adam', ['Toto', 'Titi']]

#for e in noms_supp:
#   noms.append(e)
## Résultats
# ['Jean', 'Youssef', 'Yasmina', 'Adam', 'Toto', 'Titi']

## Use extend
#noms.extend(noms_supp)
## Résultats
# ['Jean', 'Youssef', 'Yasmina', 'Adam', 'Toto', 'Titi']

## Use +=
#noms += noms_supp # ===> noms = noms + noms_supp
## Résultats
# ['Jean', 'Youssef', 'Yasmina', 'Adam', 'Toto', 'Titi']

## Inserer un elements au début de la Liste
## Use Insert
noms.insert(0,"Mohamed")
## Résultats
# ['Mohamed', 'Jean', 'Youssef', 'Yasmina', 'Adam']

### Peux-t-on utiliser la concaténation
# noms = "TOTO" + noms
## Résultats
## Error on ne peux pas concaténer un chaîne de caractère avec une Liste.
# On ne peut concaténer que des objets identiques (chaîne de caractères + chaîne de caractères ou Liste + Liste)
#noms = ["TOTO"] + noms
## Résultats
#['TOTO', 'Mohamed', 'Jean', 'Youssef', 'Yasmina', 'Adam']
## Attention à l'ordre si nécessaire
print(noms)