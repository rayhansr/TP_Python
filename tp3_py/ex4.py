essaie=0



cle=input("Entrer la cle wifi")
while essaie == 0:
    if len(cle)>8 and len(cle)<63:
        if cle.isalnum() == True:
            print("La cle est valide")
            break
        else:
            print("La cle n'est pas alphanumerique")
            essaie=0
            break
            
    else:
        print("c'est pas bon")
        essaie=0
        break