## Tester si une chaine contient des chiffres
## any /isdigit
### isdigit vérifie si la chaine contient des chiffres
#print("123".isdigit())

 #explication
## Test isdigit

def chaine_contient_des_chiffres(chaine):
    """for caractere in chaine:
        if caractere.isdigit():
            return True"""
    return any ([ c.isdigit() for c in chaine])


nom = input("Entrez un nom : ")
if nom == "":
    print("Le nom est vide.")
elif chaine_contient_des_chiffres(nom):
    print("Ce nom est invalide ! Le nom ne doit pas contenir de chiffre.")
else:
    print("Bonjour", nom)


# nom = "toto"
# contient_chiffre = any ([ c.isdigit() for c in nom])
# print(contient_chiffre)