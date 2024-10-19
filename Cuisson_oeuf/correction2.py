import time


print("""Cuisson des oeufs

      a) Oeufs à la coque : 3 mn
      b) Oeufs mollets : 6 mn
      c) Oeufs durs : 9 mn

 """)
choix = input("Votre choix : ")

duree_initiale = 0
if choix == "a":
    duree_initiale = 3*60
elif choix == "b":
    duree_initiale = 6*60
elif choix == "c":
    duree_initiale = 9*60
else:
    print("Choix invalide")
    exit()

print("Cuisson en cours: ")

for d in range(duree_initiale, 0, -1):
    mins,sec = divmod(d, 60)
    print(f"{mins:02d}:{sec:02d}", end="\r")
    time.sleep(1)

print("\nCuisson terminée")