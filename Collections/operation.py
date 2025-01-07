# LES COLLECTIONS: LISTES /TUPLES
## Operations sur éléments: min, max, in, sum


#         0         1          2        3         4
noms = ["Jean", "Youssef", "Yasmina", "Adam", "Mohamed"]

ages = [21, 20, 30, 35, 48]

#print(min(ages))
## si j'utilise min ou max avec des str il fera le tri par ordre Alphabétique
#print(max(noms))

# if 31 in ages:
#     print("Présent")
# else:
#     print("Absent")

# if "Youssef" in noms:
#     print("ok")
# else:
#     print("no OK")


# found = False
# for nom in noms:
#     if nom == "Youssef":
#         found = True
#         break
# if found:
#     print("Présent")
# else:
#     print("Absent")


# or Methode plus propre en utilisant else avec la boucle For
# for nom in noms:
#     if nom == "Youssef":
#         print("Présent")
#         break
# else:
#         print("Absent")

## SUM faire la somme de valeur Numérique
print(sum(ages))