# LES COLLECTIONS: LISTES /TUPLES
## Join & Split

## join: Rejoindre --> coller
## splite: séparer

#         0         1          2        3         4
noms = ["Jean", "Youssef", "Yasmina", "Adam", "Mohamed"]
# join
noms_joins = ", ".join(noms) ## join() prend une collection et renvoie une chaine de caractère
print(noms_joins)

# split
noms_split = noms_joins.split(", ")
print(noms_split)