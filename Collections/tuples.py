# ### Collections: (Tableaux :Array), Listes, Tuples ...

# ## Plusieurs éléments

# ## Tuples (): Immutable ==> non modifiable
# ## Liste  []: Mutable  ==> modifiable   add/remove update

# personnes = ("Yasmina", "Youssef", "Amine", "Adam")

# print(personnes)

# ### Selection 1 éléments
# print(personnes[3])

# ### Selection le dernier éléments du Tableau
# print(personnes[-1])

# ### Nombre d'éléments dans mon tableau
# print(len(personnes))

# ## Boucle pour afficher les elements du Tableau
# for i in range(0,len(personnes)):
#    print(personnes[i])

# ##Ou on peut directement faire la boucle For sur la tableau = au résultat de la boucle précédente

# for i in personnes:
#      print(i)
#  ##  une Chaîne de caratères de comporte comme un Tuple qui contiendrait les différents caractères
#      print(len(i))
#      print(i[-1])

# ### range fonctionne comme un tuple
# ### (0, 1, 2, 3, 4)
# valeur = range(0, 5)
# print(valeur[-1])