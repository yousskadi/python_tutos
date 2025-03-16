# nom, prix, ingrédients, végétarienne

class Pizza:
    def __init__(self, nom, prix,ingredients,vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " -> Végétarienne"

        print(f"Pizza {self.nom} : {self.prix} €" + veg_str)
        print(", ".join(self.ingredients))
        print()


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0 # variable de classe
    def __init__(self):
         PizzaPersonnalisee.dernier_numero += 1
         self.num = PizzaPersonnalisee.dernier_numero
         super().__init__("Personnalisée " + str(self.num), 0, [])
         self.demande_ingredient()
         self.calculprix()

    def demande_ingredient(self):
        print ("--------")
        print(f"Ingredients Pizza personnalisée numéro :{self.num}")
        while True:
            ingredient = input("Ajouter un ingrédient (ou ENTER pour terminer)")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculprix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients)* self.PRIX_PAR_INGREDIENT


############################################################

pizzas = [
    Pizza("4 Fromages", 8.5, ("brie","emental","parmesan",),True),
    Pizza("Homes", 18.5, ("boeuf","chorizo","parmesan","olive")),
    Pizza("hawaî", 14.20, ("ananas","pomme de terre","parmesan","tomate")),
    Pizza("4 saisons", 12, ("oeuf","aubergine","parmesan","tomate","courgette"),True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
]

# boucle : afficher
# (1) Les pizzas végétariennes
# for pizza in pizzas:
#     if pizza.vegetarienne:
#         pizza.Afficher()
# (2) Les pizzas non végétariennes
# for pizza in pizzas:
#     if not pizza.vegetarienne:
#         pizza.Afficher()

# (3) les pizzas qui ont de la tomates
# for pizza in pizzas:
#     if "tomate" in pizza.ingredients:
#         pizza.Afficher()

# (4) les pizzas à moins 10 €
# for pizza in pizzas:
#     if pizza.prix < 10:
#         pizza.Afficher()

# (5) triez les pizzas
# il faut transformer pizzas en une Liste [] car c'était un tuple ()
# def tri(e):
#     # return e.prix
#    # par nbre d'ingrédient
#     return len(e.ingredients)


# pizzas.sort(key=tri)
pizzas.sort(key=lambda e: len(e.ingredients))
# pizzas.sort(key=lambda e: e.prix)
# pizzas.sort(key=lambda e: e.nom)
# pizzas.sort(key=lambda e: e.vegetarienne)

for pizza in pizzas:
        pizza.Afficher()

# pizza1 = Pizza("4 Fromages", 8.5, ("brie","emental","parmesan"))

# pizza1.Afficher()
