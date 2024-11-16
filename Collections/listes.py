### Collections
#### Listes
### NB la Liste peut faire exactement ce qu'on a fait avec les tuples + faire de choses supplémantaires
## Liste  []: Mutable  ==> modifiable   add/remove update

personnes = ["Yasmina", "Youssef", "Amine", "Adam"]

nouvelle_personne = "Mohamed"

### Ajouter un élément à la Liste
personnes.append(nouvelle_personne)

### supprimer un élément à la Liste
del personnes[1]

print(personnes)

#
### utiliser un fonction pour afficher la liste et lui donner en paramètres une Liste.
def afficher_personne(c):
     for i in c:
         print(i)

# afficher_personne(personnes)

## fonction test modifier valeur int
def modifier_valeur_int(a):
    a = 10

test = 5
print(test)
modifier_valeur_int(test)
print(test)

#### Resultats la Variable test est toujours la même
#5
#5

## fonction test modifier valeur Liste
def modifier_valeur_liste(a):
    a [1] = 10

test = [0, 1, 2, 3, 4]
print(test)
modifier_valeur_liste(test)
print(test)

# resultats:
#[0, 1, 2, 3, 4]
#[0, 10, 2, 3, 4]
## ici la valeur a bien été modifiée dans la liste car c'est un container qui est donné en paramètres.
### Attention quand vous modifier une valeurs de la liste dans une fonction cela sera pris en compte quand vous sortez de celle-ci.