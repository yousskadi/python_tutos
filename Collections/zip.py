## zip
## unzip

pizzas_nom = ("4 fromages", "Calzone", "Poulet")
pizzas_prix = (10.5, 12, 16)
noms_et_prix = list(zip(pizzas_nom, pizzas_prix))
print(noms_et_prix)

for (nom, prix) in noms_et_prix:
    print(f"{nom} - {prix} €")


## unzip faire l'inverse
unzipped = list(zip(*noms_et_prix))
nom, prix = zip(*noms_et_prix)
print(nom)
print(prix)