def analyser (etat, nb_tentative):
    echec = 0
    for i in range(nb_tentative):
        for element in etat:
            if element == "oui":
                print(f"Tentative {etat}: Connexion reussie.")
            else:
                print(f"Tentative {etat}: Connexion echouee.")
                echec+=1
                if echec>3:
                    print("nah")
                    break
                    


etat = ["oui","n","n","oui","n","oui"]
nb_tentative=10
analyser(etat,nb_tentative)

#  for element in etat:
#         while echec != 3 or i<nb_tentative:
#             if element == "oui":
#                 i+=1
#                 print(f"Tentative {etat}: Connexion reussie.")
#                 continue
#             else:
#                 echec += 1
#                 i+=1
#                 print(f"Tentative {etat}: Connexion echouee.")
#                 print(echec)