#  Python fonctions: Notions Avancées
#
# Nombre Variable de Paramètres
#

# def somme(a, b):
#     return a+b

# *nbr  Permet de définir un nombre variables de paramètres

def somme(titre, *nbr):
    print("Titre: ", titre)
    resultat = 0
    for n in nbr:
        resultat += n
    return resultat


def somme(titre, **nbr):
    print("Titre: ", titre)
    resultat = 0
    for n in nbr.values():
        resultat += n
    return resultat

print(somme("Somme des notes", maths=17, geo=12, anglais=18))