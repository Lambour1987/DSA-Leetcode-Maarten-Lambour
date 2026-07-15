import random


def tuple_maken():
    bovengrens = int(input("Voer een bovengrens in: "))
    aantal_getallen = int(input("Voer het aantal getallen in: "))
    lijst = []
    for i in range(0,aantal_getallen):
        getal = random.randint(0, bovengrens)
        lijst.append(getal)
        lijst = tuple(lijst)
        print(f"KANWEG: {lijst}")
        return(tuple)


def getallen_tellen(tuple):

    for i in tuple:


tuple = tuple_maken()