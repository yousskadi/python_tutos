# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nbre_personnes = 3

liste_personne = []

for nbre in range(nbre_personnes):
    nom = input(f"nom de la personne {nbre + 1} : ")
    liste_personne.append(Personne(nom))

for personne in liste_personne:
    personne.SePresenter()