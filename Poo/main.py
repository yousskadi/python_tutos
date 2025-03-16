###
## Vos Premier PAs en Programmation Objet
###
# - Différence programmation impérative / objet
# - le plus simple possible
# - Exercices, mise en situation

## Personne (entité -> class)
# Données: nom, age
# Actions: (method)
## - SePresenter()
## - DemanderNom() input

# ------ Définition ---------------
# 1- si age == 0
## ==> Bonjour, je m'appelle toto
#  ==> On affiche pas mineur
#  ==> Si nom == ""
#  ==> Demander le Nom à l'utilisateur
#  ==> DemanderNom(...)  --> input("") --> nom

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom   ## Variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour je m'appelle Jean, j'ai 30 ans
        info_personne = "Bonjour je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + "ans"
        print(info_personne)
        if self.age != 0:
            if self.EstMajeur():
                print(f"{self.nom} est Majeur")
            else:
                print(f"{self.nom} je suis mineur")

    # EstMajeur -> True / False
    def EstMajeur(self):
        return self.age >= 18


    def DemanderNom(self):
        self.nom = input("Donner un Nom :")

#---------UTILISATION--------------
# personne1 = Personne("Youssef", 48)  # Je cree une personne
# personne2 = Personne("Yasmina", 14)

liste_personne = (Personne("Youssef", 48),
                  Personne("Yasmina", 14),
                  Personne("Tarik", 42))

for personne in liste_personne:
    personne.SePresenter()




#personne2 = Personne(age=14)
# personne3 = Personne()
# # Personne.SePresenter(personne1)
# personne1.SePresenter()
# personne2.SePresenter()  # méthode d'instance
# personne3.SePresenter()
# # personne1.EstMajeur()
# # personne2.EstMajeur()
# print("estMajeur1: ", personne1.EstMajeur())