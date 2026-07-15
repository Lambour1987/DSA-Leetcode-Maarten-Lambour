#Kanweg maar check verschil tussen zoeken op index of op waarde

import random

def genereerGetallen():
    list_A = []
    for i in range(0,3):
        willekeurig_getal = random.randrange(1,10)
        list_A.append(willekeurig_getal)
        tuple_A = tuple(list_A)
    return tuple_A

def welkgetal():
    zoekgetal = int(input("Welk getal wilt u zoeken?: "))
    return zoekgetal

def komtVoorIn(zoekgetal, lijst):
    for i in lijst:
        if i == zoekgetal:
            return True
    print("het getal is niet gevonden")
    return False

lijst = genereerGetallen()
print(lijst)
zoekgetal = welkgetal()
print(lijst)
antwoord = komtVoorIn(zoekgetal, lijst)
print(f" Getal gevonden op index {antwoord}")