## fonction demander Nom
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


## fonction demande age
def demander_age(Nom):
    age_int = 0
    while age_int == 0:
        try:
            age_int = int(input(Nom + " Quel est votre age ? "))
        except ValueError:
            print("Veuillez entrer un nombre pour l'age.")
    return age_int

## Fonction Affichage resultat

def afficher_resultat(Nom, Age, taille=0):
    print()
    print("Votre nom est " + Nom + " et vous avez " + str(Age) + " ans.")
    #print(f"Votre nom est {Nom} et vous avez {Age} ans.")
    #print("Votre nom est %s et vous avez %d ans." % (Nom, Age))
    print("l'an prochain vous aurez " + str(Age + 1) + " ans")
    #print(f"l'an prochain vous aurez {Age} ans")
    #print("l'an prochain vous aurez %d ans" % (Age + 1))



    if Age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= Age < 18:
        print("Vous êtes adolescent")
    elif Age == 1 or Age == 2:
        print("Vous êtes un bébé")
    elif Age == 18:
        print("Vous êtes tout juste majeur")
    elif Age > 60:
        print("Vous êtes sénior")
    elif Age >= 18:
        print("Vous êtes majeur")
    elif Age < 10:
        print("Vous êtes enfant")
    else:
        print("Vous êtes mineur")
# Afficher la taille
    if not taille == 0:
        print("Votre taille est de " + str(taille)+ " m")
###############################################################

## demander le nom
# nom1 = demander_nom()
# nom2 = demander_nom()
# nom = ""
# while nom == "":
#     nom = input("Quel est votre nom ? ")

## demander l'âge

#
NB_PERSONNES = 3

# boucle For
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i + 1)
    age = demander_age(nom)
    afficher_resultat(nom, age)
