###les Fonctions: Projet Questionnaire
#
# Question : Quelle est la capital de la France
# a) Marseille
# b) Nice
# c) Paris
# d) Lyon
#
# Votre reponse:
# Bonne reponse / Mauvaise Reponse
#
# Question : Quelle la capitale de L'Italie
## ...

def poser_questions(pays):
    france_city = ("Marseille", "Nice", "Paris", "Lyon")
    Italy_city = ("Rome", "Venice", "Florence", "Milan")
    print(f"Question : Quelle est la capital de la {pays} ?")
    if pays == "France":
        for i, city in enumerate(france_city, start=1):
            print(f"{i}. {city}")
        reponse1 = input("Votre reponse: ")
        if reponse1 == "3":
            print("Bonne reponse !")
        else:
            print("Mauvaise reponse.")
    elif pays == "Italie":
        for i, city in enumerate(Italy_city, start=1):
            print(f"{i}. {city}")
        reponse2 = input("Votre reponse: ")
        if reponse2 == "1":
            print("Bonne reponse !")
        else:
            print("Mauvaise reponse.")


print(poser_questions("Italie"))
poser_questions("France")

