

import random

def maak_random_rij_getallen(aantal, maximum):
    getallenlijst = []
    for getal in range(0, aantal):
        getal = random.randint(0, maximum)
        getallenlijst.append(getal)

    print(getallenlijst)

aantal= int(input("Hoeveel getallen wil je genereren?: "))
maximum = int(input("Waar is het grootste getal dat mag voorkomen?: "))
maak_random_rij_getallen(aantal, maximum)