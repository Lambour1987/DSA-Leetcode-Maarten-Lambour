import random


def genereer_getallen():
    randomlijst = [0, 0, 0]
    #
    while randomlijst[0] == randomlijst[1] or randomlijst[0] == randomlijst[2] or randomlijst[1] == randomlijst[2]:
        for i in range(3):
            randomlijst[i] = random.randrange(1, 11)
    return tuple(sorted(randomlijst))


def komt_voor_in(zoekgetal, lijst):
    getalkomtvoor = False
    for getal in lijst:
        if getal == zoekgetal:
            getalkomtvoor = True
    return getalkomtvoor


# Hier start het hoofdprogramma

# Roep de functie randomgetallen aan
# waarmee een tupel van drie random getallen gemaakt wordt
randomgetallen = genereer_getallen()
# De gebruiker gaat getallen raden
# Zet het aantal pogingen om te raden gelijk aan 0
aantal_pogingen = 0
allegetallengeraden = False
while not allegetallengeraden:
    # Hoog het aantal pogingen om te raden op met 1
    aantal_pogingen = aantal_pogingen + 1
    # Vraag input aan de gebruiker
    print("Geef 3 VERSCHILLENDE getallen tussen 1 en 10: ")
    getallen_gebruiker = []
    for i in range(3):
        inputgetal = int(input(f"Getal {i + 1}: "))
        while inputgetal < 1 or inputgetal > 10:
            print("Let op: tussen 1 en 10")
            inputgetal = int(input(f"Getal {i + 1}: "))
        getallen_gebruiker.append(inputgetal)
    correctegetallen = 0
    for getal in getallen_gebruiker:
        if komt_voor_in(getal, randomgetallen):
            correctegetallen = correctegetallen + 1
    print(f"Aantal correcte getallen = {correctegetallen}")
    if correctegetallen == 3:
        allegetallengeraden = True
        print(f"U heeft {aantal_pogingen} keer geraden")
        print("De te raden getallen waren: ", end='')
        for getal in randomgetallen:
            print(f"{getal} ", end='')







