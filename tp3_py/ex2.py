import random

temperature = random.uniform(20, 40)

# print("la valeur généré: ", temperature)

for i in range(10):
    temperature = random.uniform(20, 40)
    if temperature>35:
        print("La temperature est eleve")
        continue
    else:
        print(f"Température mesurée : {temperature:.2f}°C")
        continue