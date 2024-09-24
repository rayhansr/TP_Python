def gestion (longitude, latitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        print("Les coordonnes sont valides")
    else:
        print("Les coordonnes ne sont pas valides")

gestion(-29992, 2)
