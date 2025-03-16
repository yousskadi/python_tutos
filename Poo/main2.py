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

## EtreVivant  --> Class Parent
## Chat Personne  --> Class Enfant de EtreVivant

class EtreVivant:
    ESPECE_ETRE_VIVANT = "être vivant non identifié"

    def AfficheInfosEtreVivant(self):
        print("Info être vivant: " + Chat.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félins)"



class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain"  ## Variable de Class (1 pour toutes les Personnes)
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

class Etudiant(Personne):
    def __init__(self, nom : str, age: int, etudes: str):
        super().__init__(nom, age)
        self.etudes = etudes

    def SePresenter(self):
        super().SePresenter()
        print("Je suis étudiant en : " + self.etudes)


#---------UTILISATION--------------
# personne1 = Personne("Youssef", 48)  # Je cree une personne
# personne2 = Personne("Yasmina", 14)

liste_personne = (Personne("Youssef", 48),
                  Personne("Yasmina", 14),
                  Personne("Tarik", 42))

for personne in liste_personne:
    personne.SePresenter()
    personne.AfficheInfosEtreVivant()
    print()

chat = Chat()
chat.AfficheInfosEtreVivant()

etudiant = Etudiant("Mohamed", 17, "DEVOPS")
etudiant.SePresenter()
## Personne --> Class
##  --> Personne.ESPECE_ETRE_VIVANT
## personne1  --> Instance
##  --> self.ESPECE_ETRE_VIVANT (copie de la variable de class pour en faire une variable d'instance)
## personne2
##  --> self.ESPECE_ETRE_VIVANT
## personne3
##  --> self.ESPECE_ETRE_VIVANT