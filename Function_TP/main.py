
def est_majeur(age):
    if age <= 0:
        return False
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(num_pers):
    nom = input(f"Entrez le nom de la personne {num_pers}: ")
    age = int(input(f"Entrez l'âge de la personne {num_pers}: "))
    return nom, age

def recuperer_et_afficher_infos_personne(num_pers):
    nom, age = recuperer_infos_personne(num_pers)
    afficher_infos_personne(num_pers, nom, age)

def afficher_infos_personne(num,nom,age):
    print(f"Nom de la personne {num}: {nom} , son age est de {age}")
    print(f"Le nom comporte {len(nom)} caractères")
    if est_majeur(age):
        print(f"{nom} est majeur")
    else:
        print(f"{nom} est mineur")




nb_personnes = 3

for i in range(nb_personnes):
    recuperer_et_afficher_infos_personne(i + 1)

afficher_infos_personne(1 ,"James",41)