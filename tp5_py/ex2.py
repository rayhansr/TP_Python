import random

def surveiller ():
    debit= random.uniform(30, 50)
    seuil=40

    for i in range(10):
        debit= random.uniform(30, 50)
        if debit>seuil:
            print(f"Iteration {i}: Debit reseau {debit} Mbps depasse le seuil de {seuil}")
            continue
        else:
            print(f"Iteration {i}: Debit reseau {debit} Mbps est sous controle.")

surveiller()