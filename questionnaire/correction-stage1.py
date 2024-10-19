def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("Question")
    print("  " + question)
    print("a. " + r1)
    print("b. " + r2)
    print("c. " + r3)
    print("d. " + r4)
    print()
    reponse = input("Votre réponse : ")

    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1

    else:
        print("Mauvaise réponse")
    print()


########################

score = 0
poser_question("Quelle est la capitale de la France?", "Paris", "Lyon", "Marseille", "Toulouse","a")
poser_question("Quelle la capital de L'Italie ?", "Venise", "Naples", "Rome","Florence", "c")


print("Score final :", score)