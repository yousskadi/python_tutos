# Python Fonction: Notions Avancées
#
# Fonctions récursives

# Example 1
# def a(n, limit):
#     if n > limit:
#         return
#     print("n: ", n)
#     a(n*n, limit)

# a(2, 100000)

# Example 2

def demander_choix_user(min, max):
    reponse_str = input("Quel est votre choix entre : " + str(min) + " et " + str(max) + "?  ")
    print()
    try:
        response_int = int(reponse_str)
        if not min <= response_int <= max:
            print(f"Vous devez rentrer un nombre entre {min} et {max} ")
            return demander_choix_user(min, max)
        return response_int
    except:
        print("Erreur !!! Vous devez rentrer un nombre")
        return demander_choix_user(min, max)


choix = demander_choix_user(1, 10)
print("choix de l'utilisateur: ", choix)