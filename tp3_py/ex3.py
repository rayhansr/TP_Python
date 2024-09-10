# Nombre maximum de tentatives
max_tentatives = 3
# Compteur de tentatives
tentatives = 0

essai=0
while essai == 0:
    mdp= input("Entrer le mot de passe")
    mdp_bis=input("Remetter le mot de passe")
    if mdp_bis == mdp:
        print("Connexion reussi")
        essai=1
        break
    else:
        if tentatives != max_tentatives-1:
            essai=0
            tentatives+=1
            continue
        else:
            print("Vous avez depasse le nombre d'essaie autorise")
            essai=1
            break
