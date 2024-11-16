#  Python fonctions: Notions Avancées
#
# Différence entre Break et Return
#
# Break: permet de sortir de la boucle
        # peut être utilisé dans une fonction et dans le programme principal
        # Ne retourne pas de résultat
# Return: permet de sortir de la fonction
        # Return est spécifique au fonction
        # Peut retourner  un résultat
#
# Exemple:
#def  fonction( parametre1, parametre2, parametre3 ):
    # Traitement
    # Traitement
# Exemple 2:

def a():
    print("Debut de la fonction")
    for i in range(0, 100):
        print(i)
        if i > 20:
            print("Sortie de la boucle")
            break

    print("Fin de la fonction q")  ### Ce print sera affiché car le break sort de la boucle mais ne sort pas de la fonction

def b():
    print("Debut de la fonction")
    for i in range(0, 100):
        print(i)
        if i > 20:
            print("Sortie de la boucle")
            return
    print("fin de la fonction b")  ### ce print ne sera pas affiché car return est sortie de la fonction

b()
