from random import randint

langue=int(input("Tapez 1 pour francais et 2 pour anglais"))

nb1= randint(1, 20)
nb2= randint(1, 20)

print(nb1)
print(nb2)

if langue == 1:
    while nb1 != nb2:
        print("Les valeurs ne sont pas egaux")
        nb1= randint(1, 20)
        nb2= randint(1, 20)
        question=int(input("Voulez vous rejouer: taper 1 pour rejouer ou 2 pour quitter "))
        if question==1:
            nb1= randint(1, 20)
            nb2= randint(1, 20)
            print(nb1)
            print(nb2)
            continue
        elif question == 2:
            break
        else:
            print("La valeur rentre n'est pas bonne ")

elif langue == 2:
    while nb1 != nb2:
        print("The number aren't the same")
        nb1= randint(1, 20)
        nb2= randint(1, 20)
        question=int(input("Do you want to retry: press 1 to retry ou 2 to quit "))
        if question==1:
            nb1= randint(1, 20)
            nb2= randint(1, 20)
            print(nb1)
            print(nb2)
            continue
        elif question == 2:
            break
        else:
            continue
else:
    print("You have type a wrong value ")

if langue ==1 and nb1 == nb2:
    print("Les nombres sont egaux")
elif langue ==2 and nb1 == nb2:
    print("The number are the same")