def afficher_table_multiplication(n, min=1, max=10):
    """
    Affiche la table de multiplication de n
    """
    if min > max:
            print("Erreur: min doit être inférieur à max")
            return
    for i in range(min, max+1):
        print(f"{n} x {i} = {n*i}")

afficher_table_multiplication(5, 7, 5)