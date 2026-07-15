import random


def toon_rij_sterren(aantal):
    for i in range(aantal):
        print('*', end='')


def toon_sterren_vierkant(aantal):
    for i in range(aantal):
        toon_rij_sterren(aantal)
        print()


def toon_karakter_rij(karakter, aantal):
    for i in range(aantal):
        print(karakter, end=' ')


toon_rij_sterren(8)
print()
toon_sterren_vierkant(3)
print()
karakter = input("Welk karakter wil je dit keer gebruiken? ")
aantal = int(input('Hoe vaak wil je het zien? '))
toon_karakter_rij(karakter, aantal)
print()

# programma voor het raden van een getal
print("Raad een getal uit de reeks van 1 tot en met 10")
te_raden_getal = random.randrange(1, 10)

getal_geraden = False
aantal_pogingen = 1

while not getal_geraden:
    gok = int(input("Welk getal kiest u?: "))
    while gok < 1 or gok > 10:
        print("Kies een getal van 1 tot en met 10!")
        gok = int(input("Welk getal kiest u? "))
    if gok == te_raden_getal:
        getal_geraden = True
    else:
        if gok < te_raden_getal:
            print("Helaas, je zit te laag, doe nog een poging!")
        else:
            print("Helaas, je zit te hoog, doe nog een poging!")
        aantal_pogingen = aantal_pogingen + 1

print(f"Je hebt het geraden in {aantal_pogingen} keer.")
print("Tot de volgende keer!")
