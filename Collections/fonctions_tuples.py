###  Fontions et Tuples

def obtenir_infos():
    return "Youssef", 48, 1.72

def afficher_infos(nom, age, taille = None):
    print(f"Nom: {nom}, Age: {age}, taille: {taille}")

infos = obtenir_infos()
#print(infos)
## resultats
#('Youssef', 48, 1.72)
# print("Nom: " + infos[0])
# print("Age: " + str(infos[1]))
# print("Taille: " + str(infos[2]))

## resultats
# Nom: Youssef
# Age: 48
# Taille: 1.72

#### Autres méthode plus rapide en créant les 3  variables directement
nom, age, taille = obtenir_infos()
print(f"Nom: {nom}, Age: {age}, taille: {taille}")
# resultats
# Nom: Youssef, Age: 48, taille: 1.72

## Utilisation de la fonction avec les paramètres
afficher_infos(nom, age, taille)
# resultats
# Nom: Youssef, Age: 48, taille: 1.72

## si je souhaite passer le tuple directement je dois ajouter "*"devant sinon Erreur.
afficher_infos(*obtenir_infos())
## ou

print(infos)  ## Affiche un Tuple ==> 1 seul paramètres
print(*infos) ## Affiche 3 ==> 3 paramètres c comme si on avait passé print(info[0], info[1], info[2]). "Unpack tuple"
print(infos[0], infos[1], infos[2])  ## même résulat que print(*infos)

afficher_infos(*infos)