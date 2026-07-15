#Rij van random getallen

import random


def maak_random_rij_getallen(aantal, maximum):
    print("Dit zijn de getallen: ")
    for i in range(0,aantal):
        getal = random.randint(1,maximum)
        print(getal, end=" ")

aantal = int(input("Hoeveel getallen wil je genereren? "))
maximum = int(input("Wat is het grootste getal dat mag voorkomen? "))

maak_random_rij_getallen(aantal, maximum)