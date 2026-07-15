import random

def genereerGetallen():
    getallen_lijst = []
    for i in range(0,3):
        getal = random.randint(0,10)
        getallen_lijst.append(getal)
    getallen_tuple = tuple(getallen_lijst)
    return getallen_tuple

def komtVoorIn(zoekgetal, lijst):
    for getal in lijst:
        if getal == zoekgetal:
            return True
    else:
        return False


def vraaggebruiker():
    for i in range(0,3):
        getal = int(input(f"getal {i} is: "))
        print(getal)

lijst = genereerGetallen()
print(lijst)
antwoord = komtVoorIn(3, lijst)
print(antwoord)
vraaggebruiker()

