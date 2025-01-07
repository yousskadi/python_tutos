## LES COLLECTIONS: LISTES /TUPLES
## Exercice "in insensible à la casse"


def element_dans_liste(element, liste):
    """for item in liste:
        if item.lower() == element.lower():
            return True
    return False"""
    return element.lower() in [item.lower() for item in liste]

#         0         1          2        3         4         5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Claire"]

element_nom = input("Entrez un nom: ")
if element_dans_liste(element_nom, noms):
    print(f"{element_nom} est dans la liste")
else:
    print(f"{element_nom} n'est pas dans la liste")