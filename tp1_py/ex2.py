from random import randint

nb1= randint(1, 100)
nb2= randint(1, 100)

print(nb1)
print(nb2)

somme=nb1+nb2

utilisateur=int(input("Entrer la somme des deux nombres "))

try:
    if somme==utilisateur:
        print("Bien joue")
    else:
        print("Reesayer")
except:
    print("La saisie n'est pas valide")