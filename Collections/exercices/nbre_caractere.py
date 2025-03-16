## LES COLLECTIONS: LISTES /TUPLES
## Exercice "Nombre Total de Caractères"


#         0         1          2        3         4         5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Claire"]

## 1 - for /len
'''
s = 0
for nom in noms:
    nbr_caractere = len(nom)
    s += nbr_caractere
print("Nbre Total de caractères:", s)
'''
## 2 - Completion de liste + sum
# longueur_noms = []
# for nom in noms:
#     longueur_noms.append(len(nom))
# print(longueur_noms)
# print(sum(longueur_noms))
# longueur_noms = [len(nom) for nom in noms]
# print(longueur_noms)
# print("Nbre Total de caractères", sum(longueur_noms))

## 3 - Join /len
print("Nbre Total de caractères",len("".join(noms)))