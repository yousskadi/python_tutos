## LISTES -ALGO : Valeur la plus petite

nom_chauffeur =  ["Patrick", "Sandy", "Patrick", "Sandy", "Jean", "Patrick", "Sandy", "Jean"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 1.4, 7.1, 1.1, 0.6]

# index_min

dist_min = distance_chauffeur_km[0]
# for distance in distance_chauffeur_km:
#     if distance < dist_min:
#         dist_min = distance
#         index_min = distance_chauffeur_km.index(dist_min)
## OR
# for i in range(len(distance_chauffeur_km)):
#     if distance_chauffeur_km[i] < dist_min:
#         dist_min = distance_chauffeur_km[i]
#         index_min = i
#         nom_min = nom_chauffeur[i]


# print("Distance Minimal: ", dist_min, "km")
# print("Index de la distance minimal:", index_min)
# print("Nom du Chauffeur : ", nom_chauffeur[index_min])

## OR
## on peut trier les éléments de la liste
# distance_chauffeur_km.sort()
# print(distance_chauffeur_km[0])
## Pb les index des distances ne correspondent plus à ceux des chauffeurs
## on peut créer une liste des distances triées
#distance_chauffeur_km_triee = sorted(distance_chauffeur_km)

## une meilleur façon de faire c créer des paires nom, distance
noms_et_distances = [(nom_chauffeur[i], distance_chauffeur_km[i]) for i in range(len(nom_chauffeur))]
#noms_et_distance = [("Patrick", 1.5), ("Youssef", 0.5), ("Miloud", 2.2), ("Olivier", 1.1)]
# print(noms_et_distances[0])
# print(noms_et_distances[0][1])

### V2
# nom_et_distance_min = noms_et_distances[0]
# for nom_et_distance in noms_et_distances:
#     if nom_et_distance[1] < nom_et_distance_min[1]:
#         nom_et_distance_min = nom_et_distance

# print(f"Le chauffeur: {nom_et_distance_min[0]} est à {nom_et_distance_min[1]} km")