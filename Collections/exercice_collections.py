### Listes - Exercie: Demander Noms de personnes

## demander des noms de personnes
# Boucle infinie, sort quand le nom est vide == ""  ==> break
# seulement à la fin on afficher la liste

noms = []
while True:
    nom = input("Nom: ")
    if nom == "":
        break
    noms.append(nom)

#print(noms)
print()
print("Affichage des noms")
print("------------------")
noms.sort() ## trier par ordre Alphabétique Attention les lettre corresponde à des nombre  et
#la Majuscule a un nombre différent de la minuscule d'abord A-Z a-z
# le tri se fait directement dans la liste - dit "in place"
for nom in noms:
    print(" " + nom)