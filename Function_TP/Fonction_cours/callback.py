#  Python fonctions: Notions Avancées
#
# CALLBACK
#

# Exemple 1 :
# def ma_fonction():
#     print("Je suis une fonction")
#     return 1

# a = 5
# b1 = ma_fonction()
# b2= ma_fonction

# print(b1)
# print(b2)

# print(b2())

def afficher_table(n, operator_str, operation_cbk):
    for i in range(1, 11):
        print(i, operator_str, n, "=", operation_cbk(i, n))

# def afficher_table_addition(n, operator_str):
#     for i in range(1, 11):
#         print(i, operator_str, n, "=", table_addition(i, n))

def multi_callback(a, b):
    resultat = a*b
    return resultat

def add_callback(a, b):
    resultat = a+b
    return resultat

def power_callback(a, b):
    return pow(a, b)


# afficher_table(2, "x", multi_callback)
# print()
# afficher_table(2, "+", add_callback)
# print()
# afficher_table(2, "^", power_callback)

### Fonction LAMBDA

afficher_table(2, "x", lambda a, b: a*b)
print()
afficher_table(2, "+", lambda a, b: a+b)
print()
afficher_table(2, "^", lambda a, b: pow(a, b))