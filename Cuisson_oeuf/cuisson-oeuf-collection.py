import time


# duree = 10
# min = d//60
# sec = d%60
# print(f"{min}:{sec}")


CHOIX_CUISSON = (
    ("Oeufs à la coque", 3*60),
    ("Oeufs mollets", 6*60),
    ("Oeufs durs", 9*60),
    ("Steak à point", 30),
    ("test1", 5),
    ("test1", 11)
)

def temps_sec_str(t):
    min = t//60
    sec = t-min*60
    min_unit = "minutes"
    sec_unit = "secondes"
    if min <= 1:
        min_unit = "minute"
    if sec == 1:
        sec_unit = "seconde"
    r = ""
    if min > 0:
        r += f"{min} {min_unit}"
    if sec > 0:
        if len(r) > 0:
            r += ""
        r += f" {sec} {sec_unit}"
    return r

### fonction Demande choix utilisateur et vérification des valeurs données
def demander_valeur_min_max(min, max):
    valeur = input(f"Entrez votre choix entre {min} et {max}: ")
    try:
        valeur_int = int(valeur)
    except:
        print("Choix invalide. Veuillez réessayer.")
        return demander_valeur_min_max(min, max)

    if not (min <= valeur_int <= max):
        print(f"Choix invalide. Entrez votre choix entre {min} et {max}: ")
        return demander_valeur_min_max(min, max)
    return valeur_int



##############################################################################

##############################################################################

### Affichage du Menu
print("Choix Cuisson")
index_choix = 1
for choix in CHOIX_CUISSON:
    print(f"{index_choix} - {choix[0]} : {temps_sec_str(choix[1])}")
    index_choix += 1

### Choix utilisateur

choix = demander_valeur_min_max(1, len(CHOIX_CUISSON))
choix = CHOIX_CUISSON[choix-1]
duree = choix[1]
### Choix utilisateur


while duree > 0:
    for i in range(10):
        time.sleep(1)
        print(".",end="",flush=True)
        duree -= 1
        if duree == 0:
            break

    if duree == 0:
        break
    min = duree//60
    sec = duree%60
    print()
    print(f"Temps restant: {min:02d}:{sec:02d}",end="",flush=True)

print("\nCuisson terminée")
