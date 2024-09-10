note_int= 100
while note_int == 100:
    moyenne=input("Quelle est votre moyenne ")
    try:
        note_int = int(moyenne)
    except:
        print("La valeur n'est pas un chiffre ou un nombre")
    else:
        if note_int>20:
            print("La note ne peux pas depasser 20")
            note_int= 100
        elif note_int > 18:
            print("Excellent")
        elif 14<=note_int<18:
            print("Tres bien")
        elif 10<=note_int<14 :
            print("Assez bien")
        elif 5<=note_int<10:
            print("Insuffisant")
        elif 0<=note_int<5:
            print("Catastrophque")
        elif note_int<0:
            print("La note ne peux pas avoir moins de 0")
            note_int= 100

