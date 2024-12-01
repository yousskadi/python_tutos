### Fonction qui permet de gérer les errreurs lors de la reponse de l'utlisateur

def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input("Votre réponse entre " + str(min) + " et " + str(max) + " : ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer un nombre")
    ## fonction recursive si il y a des erreurs la fonction se rappel elle-même
    return demander_reponse_numerique_utilisateur(min, max)

############################################

def poser_question(question):
    titre_question = question[0]
    choix = question[1]
    choix_bonne_reponse = question[2]
    print("Question: ")
    print(" " + titre_question)

    for i in range(len(choix)):
        print(" " + str(i+1) + "- " + choix[i])

    print()
    resultat_response_correcte = False
    # reponse_str = input("Votre réponse entre 1 et " + str(len(choix)) + " : ")
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))
    if choix[reponse_int - 1].lower() == choix_bonne_reponse.lower():
        print("Bonne réponse")
        resultat_response_correcte = True

    else:
        print("Mauvaise réponse")
    print()
    return resultat_response_correcte

###############################
### Fonction qui gère un questionnaire avec plusieurs questions

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

########################

## Créer un tuple avec toute les questions
questionnaire = (
        ("Quelle est la capitale de la France ?", ("Paris", "Lyon", "Marseille", "Toulouse","Lille"), "Paris"),
        ("Quelle est la capitale de l'Italie ?", ("Venise", "Naples", "Rome", "Florence"), "Rome"),
        ("Quelle est la capitale de la Belgique ?", ("Bruxelles", "Liège", "Namur"), "Bruxelles")
        )



lancer_questionnaire(questionnaire)
