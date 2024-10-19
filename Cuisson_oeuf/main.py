import time


# duree = 10
# min = d//60
# sec = d%60
# print(f"{min}:{sec}")


print("Programme Temps de Cuisson des Oeufs")
print("a - Oeufs à la coque : 3 mn")
print("b - Oeufs mollets : 6 mn")
print("c - Oeufs durs : 9 mn")

while True:
    choix = input("Votre choix: ")
    if choix == "a" or choix == "b" or choix == "c":
        break
    print("Choix invalide. Veuillez réessayer.")


duree = 0
if choix == "a":
    duree = 3*60
elif choix == "b":
    duree = 6*60
else:
    duree = 9*60


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


# for i in range(d):
#     time.sleep(1)
#     print(f"{min}:{sec}")
#     print(".", end="", flush=True)
#     # print(f"{min}:{sec}")
#     # sec -= 10
# print("\nDone!")
