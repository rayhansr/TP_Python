def mdp (mot_de_passe, tentative):
    bonmdp = "admin"
    nb_restant=0
    for i in range(tentative):
        if mot_de_passe == bonmdp:
            print("Connection reussi")
            break
        else:
            nb_restant+=1
            tent=tentative-nb_restant
            print(f"Connetion rate, il vous reste {tent} essaie")

mdpp = "adin"
mdp(mdpp, 3)
