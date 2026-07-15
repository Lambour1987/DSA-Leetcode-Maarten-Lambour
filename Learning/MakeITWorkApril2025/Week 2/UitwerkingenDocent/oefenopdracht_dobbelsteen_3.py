"""
Dit programma toont random getallen in de vorm van een dobbelsteen. De
gebruiker kan zelf aangeven welk karakter gebruikt moet worden om het
oog van de dobbelsteen weer te geven. Het programma gaat door totdat
de waarde 6 is gegooid.
"""
import random


def toon_worp(aantal, karakter):
    """
    Deze functie print het patroon van de waarde van de dobbelsteen en gebruikt
    het karakter in de variabele oog als het oog van de dobbelsteen
    :param aantal: waarde van de dobbelsteen (int)
    :param karakter: teken voor het oog van de dobbelsteen (str)
    :return: GEEN
    """
    # maak f'strings voor de verschillende regels van kanten van de dobbelsteen
    # ga uit van een breedte van 5
    links = f'{karakter}'
    rechts = f'{karakter:>5}'
    midden = f'{karakter:^5}'
    links_rechts = f'{karakter:<4}{karakter}'
    # print per waarde het specifieke dobbelsteenpatroon obv oog
    if aantal == 1:
        print()
        print(midden)
        print()
    elif aantal == 2:
        print(links)
        print()
        print(rechts)
    elif aantal == 3:
        print(links)
        print(midden)
        print(rechts)
    elif aantal == 4:
        print(links_rechts)
        print()
        print(links_rechts)
    elif aantal == 5:
        print(links_rechts)
        print(midden)
        print(links_rechts)
    elif aantal == 6:
        print(links_rechts)
        print(links_rechts)
        print(links_rechts)
    # einde functie toon_worp()


# start van het hoofdprogramma
# vraag de gebruiker welk karakter gebruikt moet worden voor het oog
oog = input("Welk karakter moet ik gebruiken voor het oog: ")

# zet waarde op 0 zodat het while statement in ieder geval 1x uitgevoerd wordt
waarde = 0
# zolang er geen 6 is gevallen, kies een nieuwe random waarde en
# print de waarde van de dobbelsteen
while waarde != 6:
    waarde = random.randrange(1, 7)
    toon_worp(waarde, oog)
